import re

from openai import OpenAI
from config import OPENROUTER_API_KEY

from tools.calculator import *
from tools.datetime_tool import get_datetime
from tools.summarizer import summarize

from rag.document_loader import load_documents
from rag.embeddings import create_chunks, generate_embeddings
from rag.rag_pipeline import RAGPipeline


# -----------------------------
# OpenRouter Client
# -----------------------------

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


# -----------------------------
# Load RAG Documents
# -----------------------------

print("Loading documents...")

documents = load_documents("data")

chunks = create_chunks(documents)

embedding_model, embeddings = generate_embeddings(chunks)

rag = RAGPipeline(
    chunks,
    embeddings
)


# -----------------------------
# Conversation Memory
# -----------------------------

memory = []


# -----------------------------
# AI Agent Function
# -----------------------------

def run_agent(user):

    global memory

    if not user or not user.strip():
        return "Please enter a question or request."

    # Show history
    if user.lower() == "history":

        if len(memory) == 0:

            return "No conversation history yet."

        return "\n".join(memory)


    # Create previous conversation context

    history_text = "\n".join(memory)


    # Ask LLM to select tool

    prompt = f"""
You are an AI Agent.

Previous Conversation:
{history_text}

User Request:
{user}

Available Tools:

calculator
datetime
summarizer
rag

Rules:

- Mathematical calculations → calculator
- Current date or time → datetime
- Summarizing text → summarizer
- Questions about uploaded PDF documents → rag

Reply ONLY with one word:
calculator
datetime
summarizer
rag
"""


    try:

        response = client.chat.completions.create(
            model="tencent/hy3:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

    except Exception:

        return (
            "AI service is currently unavailable. "
            "Please check the API configuration and try again."
        )


    tool = response.choices[0].message.content.strip().lower()


    print("Selected Tool:", tool)


    # -----------------------------
    # Calculator Tool
    # -----------------------------

    if tool == "calculator":
        numbers = re.findall(r"\d+(?:\.\d+)?", user)

        if len(numbers) < 2:
            return "Please provide two numbers for calculation."

        a = float(numbers[0])
        b = float(numbers[1])

        if (
            "add" in user.lower()
            or "plus" in user.lower()
            or "+" in user
        ):
            result = add(a, b)

        elif (
            "subtract" in user.lower()
            or "subtracted" in user.lower()
            or "minus" in user.lower()
            or "-" in user
        ):
            result = subtract(a, b)

        elif (
            "multiply" in user.lower()
            or "multiplied" in user.lower()
            or "multiplication" in user.lower()
            or "times" in user.lower()
            or "×" in user
            or "*" in user
        ):
            result = multiply(a, b)

        elif (
            "divide" in user.lower()
            or "divided" in user.lower()
            or "division" in user.lower()
            or "/" in user
        ):
            result = divide(a, b)

        else:
            return "Please specify an operation."

        answer = f"Answer: {result}"

        memory.append(
            f"User: {user}\nAssistant: {answer}"
        )

        if len(memory) > 5:
            memory.pop(0)

        return answer

    # -----------------------------
    # Date & Time Tool
    # -----------------------------

    elif tool == "datetime":

        dt = get_datetime()

        answer = f"""
Current Date: {dt['date']}
Current Time: {dt['time']}
"""

        memory.append(
            f"User: {user}\nAssistant: {answer}"
        )

        return answer


    # -----------------------------
    # Summarizer Tool
    # -----------------------------

    elif tool == "summarizer":

        text = user

        if ":" in user:
            text = user.split(":", 1)[1].strip()

        answer = summarize(text)

        memory.append(
            f"User: {user}\nAssistant: {answer}"
        )

        if len(memory) > 5:
            memory.pop(0)

        return answer
    # -----------------------------
    # RAG Tool
    # -----------------------------

    elif tool == "rag":

        query_embedding = embedding_model.encode(
            user
        ).tolist()


        results = rag.search(
            query_embedding,
            n_results=2
        )


        retrieved_docs = "\n".join(
            results["documents"][0]
        )


        source = results["metadatas"][0][0]


        response = client.chat.completions.create(

            model="tencent/hy3:free",

            messages=[

                {
                    "role": "system",

                    "content":
                    "Answer ONLY from the given context. "
                    "If the answer is not found, say "
                    "'Not found in the document.'"
                },

                {

                    "role": "user",

                    "content": f"""
Context:
{retrieved_docs}

Question:
{user}
"""
                }

            ]

        )


        answer = response.choices[0].message.content


        final_answer = f"""
Answer:
{answer}

Source:
Document: {source['file']}
Page: {source['page']}
"""


        memory.append(
            f"User: {user}\nAssistant: {final_answer}"
        )


        if len(memory) > 5:

            memory.pop(0)


        return final_answer


    else:

        return "I don't know which tool to use."
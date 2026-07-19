# AI Knowledge Assistant

An end-to-end AI application that combines Retrieval-Augmented Generation (RAG), AI tools, and conversation memory.

## Features

- Ask questions from PDF documents
- Perform calculations
- Get current date and time
- Summarize text
- Maintain conversation memory
- Display document source information
- Single Streamlit chat interface

## Technologies Used

- Python
- Streamlit
- OpenRouter API
- ChromaDB
- Sentence Transformers
- PyPDF

## Project Structure

ai-knowledge-assistant/
├── app.py
├── agent.py
├── config.py
├── tools/
├── rag/
├── data/
└── vector_db/

## Setup

Install dependencies:

pip install -r requirements.txt

Create a `.env` file:

OPENROUTER_API_KEY=your_api_key_here

Run the application:

streamlit run app.py
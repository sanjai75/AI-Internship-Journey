# RAG Document Assistant

A simple Retrieval-Augmented Generation (RAG) application built using Python, LangChain, ChromaDB, and Google Generative AI/OpenRouter.

## Project Structure

- app.py
- data/
- vector_db/
- requirements.txt
- README.md

## Purpose

This project answers questions from PDF documents using RAG instead of relying only on an LLM's pre-trained knowledge.
## Setup

1. Clone the repository.
2. Install requirements:
   pip install -r requirements.txt
3. Create a `.env` file:

OPENROUTER_API_KEY=your_api_key_here

4. Run:
python app.py
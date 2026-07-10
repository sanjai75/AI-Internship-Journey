# RAG Document Assistant

## Project Overview

RAG Document Assistant is a simple Retrieval-Augmented Generation (RAG) application built using Python, ChromaDB, Sentence Transformers, and the OpenRouter API. It allows users to upload a PDF document, ask questions, and receive answers based only on the document's content.

## Features

- Load PDF documents
- Split documents into text chunks
- Generate embeddings using Sentence Transformers
- Store embeddings in ChromaDB
- Retrieve relevant document chunks
- Generate answers using OpenRouter LLM
- Reduces hallucinations by using document context
- Supports multiple PDF documents

## Technologies Used

- Python 3.14
- ChromaDB
- Sentence Transformers
- OpenRouter API
- PyPDF
- python-dotenv

## Project Structure

```
rag-document-assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── sample.pdf
└── vector_db/
```

## Installation

1. Clone the repository.

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your API key:

```text
OPENROUTER_API_KEY=your_api_key_here
```

4. Run the application:

```bash
python app.py
```

## Sample Output

```
Ask a question about the PDF:
What is Python?

Answer:
Python is a high-level, interpreted programming language.
```

## Purpose

This project demonstrates how Retrieval-Augmented Generation (RAG) improves the accuracy of AI responses by retrieving relevant information from a PDF document before generating an answer.

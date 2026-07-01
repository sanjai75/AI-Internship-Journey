# AI Programming Chatbot

## Project Overview

This project is a simple AI-powered chatbot built using Python and the OpenRouter API. The chatbot allows users to ask programming-related questions and receive AI-generated responses. It also includes additional features such as chat history, help commands, screen clearing, conversation memory, date & time display, and improved error handling.

---

## Features

* Welcome message with user name
* AI-powered question answering
* Conversation history
* Save chat history to a text file
* Display date and time for each response
* `/help` command
* `/clear` command
* Exit command
* Loading message while waiting for AI response
* Better error handling

---

## Technologies Used

* Python 3
* OpenRouter API
* OpenAI Python Library
* VS Code
* Git & GitHub

---

## How to Install

1. Install Python 3.
2. Install the required package:

```
pip install openai
```

3. Create an OpenRouter account.
4. Generate an API Key.
5. Replace `YOUR_OPENROUTER_API_KEY` in the code with your API key.

---

## How to Run

Open the terminal inside the project folder and run:

```
python ai_chatbot.py
```

---

## Sample Output

```
=======================================================
          AI PROGRAMMING ASSISTANT
=======================================================

Enter your name: Sanjai

Welcome Sanjai!
Ask me anything about Programming.

You: What is Python?

AI:
Python is a high-level programming language that is easy to learn and widely used for web development, AI, automation, and data analysis.
```

---

## Challenges Faced

* Understanding how AI APIs work.
* Generating and managing API keys securely.
* Handling API rate limit errors.
* Fixing GitHub Push Protection issues caused by exposed API keys.
* Integrating the OpenRouter API with Python.

---

## Future Improvements

* Add colored terminal output.
* Support multiple AI models.
* Create a graphical user interface (GUI).
* Add voice input and voice responses.
* Store chat history in a database.
* Improve conversation memory.

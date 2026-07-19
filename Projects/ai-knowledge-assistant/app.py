import streamlit as st

from agent import run_agent


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="🤖"
)


# -----------------------------
# Title
# -----------------------------

st.title("🤖 AI Knowledge Assistant")

st.write(
    "Ask questions from your documents or use AI tools."
)


# -----------------------------
# Conversation History
# -----------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# -----------------------------
# Chat Input
# -----------------------------

user_input = st.chat_input(
    "Ask a question..."
)


if user_input:

    # Display user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )


    with st.chat_message("user"):

        st.write(user_input)


    # Run AI Agent

    with st.chat_message("assistant"):

        with st.spinner(
            "Thinking..."
        ):

            response = run_agent(
                user_input
            )


        st.write(response)


    # Store assistant response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
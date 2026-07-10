import streamlit as st

st.set_page_config(page_title="RAG Document Assistant")

st.title("📄 RAG Document Assistant")

st.write("Ask questions about your PDF documents.")

question = st.text_input("Enter your question:")

if st.button("Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        st.success("Question received!")

        st.write("### Your Question")
        st.write(question)

        st.info(
            "For the internship demo, this UI is connected to your existing RAG logic in app.py.\n"
            "To make it fully interactive, the RAG code should be moved into reusable functions and called from here."
        )
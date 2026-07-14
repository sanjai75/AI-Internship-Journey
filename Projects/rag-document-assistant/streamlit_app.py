import streamlit as st

st.set_page_config(page_title="RAG Document Assistant")

st.title("📄 RAG Document Assistant")

st.write("Ask questions about your PDF documents.")

uploaded_files = st.file_uploader(
    "Upload one or more PDF files",
    type="pdf",
    accept_multiple_files=True
)

if "history" not in st.session_state:
    st.session_state.history = []

question = st.text_input("Enter your question:")

if st.button("Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        st.success("Question received!")

        st.write("### Your Question")
        st.write(question)
        st.write("### Answer")
        st.write("Demo answer from RAG")
        st.write("### Source")
        st.write("python_notes.pdf (Demo)")

        st.info(
            "For the internship demo, this UI is connected to your existing RAG logic in app.py.\n"
            "To make it fully interactive, the RAG code should be moved into reusable functions and called from here."
        )
        st.session_state.history.append({
            "question": question,
            "answer": "Demo answer from RAG",
            "source": "python_notes.pdf"
        })
st.write("---")
st.subheader("Chat History")

for chat in st.session_state.history:
    st.write("Question:", chat["question"])
    st.write("Answer:", chat["answer"])
    st.write("Source:", chat["source"])
    st.write("---")
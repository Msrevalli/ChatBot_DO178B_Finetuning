import streamlit as st
from transformers import pipeline, GPT2Tokenizer, GPT2LMHeadModel
import PyPDF2
import docx

# Load the GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Define the chatbot pipeline
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Function to read text files
def read_txt(file):
    return file.read().decode("utf-8")

# Function to read PDF files
def read_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    content = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        content += page.extract_text()
    return content

# Function to read DOCX files
def read_docx(file):
    doc = docx.Document(file)
    content = ""
    for para in doc.paragraphs:
        content += para.text + "\n"
    return content

# Streamlit App
st.title("Chatbot using GPT-2 and Document Upload")

# Upload document section
st.subheader("Upload Your Document")
uploaded_files = st.file_uploader("Choose a text file", type=["txt", "pdf", "docx"], accept_multiple_files=True)

# Extract document content
document_content = ""
if uploaded_files:
    for uploaded_file in uploaded_files:
        if uploaded_file.type == "text/plain":
            document_content += read_txt(uploaded_file) + "\n"
        elif uploaded_file.type == "application/pdf":
            document_content += read_pdf(uploaded_file) + "\n"
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            document_content += read_docx(uploaded_file) + "\n"

# User input section
st.subheader("Chat with the Document")
user_input = st.text_area("Enter your message:")

# Generate chatbot response when button is clicked
if st.button("Send"):
    if document_content:
        # Include document content as part of the context
        response = chatbot(user_input, max_length=50, num_return_sequences=1, context=document_content)[0]["generated_text"]
    else:
        response = chatbot(user_input, max_length=50, num_return_sequences=1)[0]["generated_text"]

    st.write("Chatbot:", response)

    # Optional: Display chatbot's history
    history = [(user_input, response)]
    for message in history:
        st.write(f"You: {message[0]}")
        st.write(f"Chatbot: {message[1]}")

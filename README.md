# ChatBot_DO178B_Finetuning

# Chatbot using GPT-2 and Document Upload

This project is a Streamlit application that allows users to upload documents and chat with a GPT-2 based chatbot. The chatbot uses the content of the uploaded documents to provide context-aware responses.

## Features

- Upload text files, PDFs, or DOCX documents.
- Interact with a GPT-2 based chatbot that uses the content of the uploaded documents to generate responses.
- Simple and intuitive web interface using Streamlit.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to access the application.

## How It Works

- **Document Upload:** Users can upload text files (`.txt`), PDF files (`.pdf`), and DOCX files (`.docx`). The content of these files is extracted and used to provide context for the chatbot.
- **Chat Interface:** Users can enter messages in a text area and click the "Send" button to interact with the chatbot. The chatbot's responses are generated based on the user's input and the content of the uploaded documents.

## File Structure

- `app.py`: The main Streamlit application file.
- `requirements.txt`: Lists the dependencies required to run the application.
- `README.md`: This readme file.

## Dependencies

- `streamlit`: For creating the web interface.
- `transformers`: Hugging Face library to use GPT-2.
- `torch`: PyTorch, required for the GPT-2 model.
- `PyPDF2`: For reading PDF files.
- `python-docx`: For reading DOCX files.

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing the GPT-2 model and the `transformers` library.
- [Streamlit](https://streamlit.io/) for making it easy to create interactive web applications.

## License

This project is licensed under the MIT License.

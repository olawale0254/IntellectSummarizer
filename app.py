import streamlit as st
import os
import tempfile
from src.pytesseract_ocr import PDFToTextConverter
from src.summarizer import TextSummarizer

# Initialize the summarizer
summarizer = TextSummarizer()

# Custom CSS for styling
st.markdown("""
    <style>
    .reportview-container {
        background: url("https://source.unsplash.com/weekly?water");
        background-size: cover;
    }
    .sidebar .sidebar-content {
        background: rgba(255, 255, 255, 0.8);
    }
    h1 {
        color: #0E1117;
    }
    .stButton>button {
        color: #ffffff;
        background-color: #0E1117;
        border-radius: 20px;
        border: 1px solid #9c27b0;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: bold;
    }
    .stTextArea>textarea {
        border-radius: 10px;
        border: 2px solid #9c27b0;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and introduction
st.title("PDF Text Summarizer")

# Sidebar for selection
option = st.sidebar.radio(
    "Choose the input method:",
    ("Upload PDF", "Enter Text")
)

# Process PDF
def process_pdf(file_path):
    converter = PDFToTextConverter(file_path)
    return converter.convert()

# Main container
with st.container():
    st.write("## INTELLECTSUMMARIZER")
    st.markdown("""
This tool allows you to extract and summarize text from PDF documents or directly from your input. 
Choose your preferred method and get concise summaries quickly and efficiently.
""")

    # Handle PDF upload
    if option == "Upload PDF":
        st.markdown("### Upload your PDF")
        uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

        if st.button('Summarize PDF'):
            if uploaded_file is not None:
                with st.spinner('Extracting and summarizing...'):
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                        tmp.write(uploaded_file.getvalue())
                        extracted_text = process_pdf(tmp.name)

                    os.remove(tmp.name)

                    if extracted_text:
                        summarized_text = summarizer.summarize(extracted_text)
                        st.markdown("### Original Text:")
                        st.text_area("Extracted Text:", value=extracted_text, height=150, disabled=True)
                        st.markdown("### Summarized Text:")
                        st.text_area("Summary:", value=summarized_text, height=100, disabled=True)
                    else:
                        st.error("No text extracted from PDF.")
            else:
                st.error("Please upload a PDF file.")

    # Handle text input
    elif option == "Enter Text":
        st.markdown("### Enter your text")
        user_input_text = st.text_area("Input your text here:")

        if st.button('Summarize Text'):
            if user_input_text:
                summarized_text = summarizer.summarize(user_input_text)
                # print(summarized_text)
                st.markdown("### Summarized Text:")
                st.text_area("Summary:", value=summarized_text, height=100, disabled=True)
            else:
                st.error("Please enter some text to process.")

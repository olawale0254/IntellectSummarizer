# PDF Text Summarizer

## Overview

PDF Text Summarizer is a Streamlit-based application that allows users to extract and summarize text from PDF documents or input text directly. It's designed to simplify the process of understanding large documents by providing concise summaries.

## Features

- **PDF Text Extraction**: Upload PDF documents to extract text.
- **Text Summarization**: Summarize extracted or input text for quick comprehension.
- **User-Friendly Interface**: Easy-to-use sidebar for method selection and interactive elements for a better user experience.

## Project Architecture/Workflow

### Components

1. **Streamlit Application (`app.py`)**: The frontend interface where users interact with the application.
2. **Text Extraction Module (`src/pytesseract_ocr.py`)**: Extracts text from uploaded PDF files.
3. **Text Summarization Module (`src/summarizer.py`)**: Summarizes the extracted or input text.

### Workflow

1. **Start**: User chooses to upload a PDF or input text directly.
2. **Processing**:
    - If a PDF is uploaded, the `PDFToTextConverter` extracts text from the PDF.
    - If text is input directly, it is taken as is for summarization.
3. **Summarization**: The `TextSummarizer` generates a concise summary of the provided text.
4. **Display**: The original text (if extracted) and the summarized text are displayed to the user.

## How to Use

1. **Start the Application**: Run `streamlit run app.py` in the terminal.
2. **Choose Input Method**: Use the sidebar to select between uploading a PDF or entering text.
3. **Upload or Enter Text**: Either upload a PDF file or type text into the provided text area.
4. **Summarize**: Click the 'Summarize' button to process and view the summary.

## Screenshots/Clippings

Here are some screenshots showing different stages of the PDF Text Summarizer application:

### Start Screen
![Start Screen](URL_TO_YOUR_START_SCREEN_IMAGE)


## Installation and Setup

Follow these steps to get the application up and running:

1. **Clone the repository**:
    ```
    git clone https://github.com/olawale0254/IntellectSummarizer.git

2. **Navigate to the project directory**:
    ```
    cd IntellectSummarizer

3. **Install dependencies**:

    ```
    pip install -r requirements.txt

4. **Run the application**:
    ```
    streamlit run app.py
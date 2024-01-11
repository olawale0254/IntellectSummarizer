from pypdf import PdfReader

class PDFToTextConverter:
    def __init__(self, pdf_file_path):
        self.pdf_file_path = pdf_file_path

    def convert(self):
        try:
            reader = PdfReader(self.pdf_file_path)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:  # Check if text extraction is successful
                    text += page_text + "\n"
            return text
        except Exception as e:
            return str(e)  # Return the exception message for debugging


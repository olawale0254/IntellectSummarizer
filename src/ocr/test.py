from pytesseract_ocr import PDFToTextConverter

pdf_path = "/Users/olawaleabimbola/Documents/IntellectSummarizer/src/ocr/test.pdf"
converter = PDFToTextConverter(pdf_path)
text = converter.convert()
print(text)

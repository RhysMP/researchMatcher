from PyPDF2 import PdfReader


def convert_pdf_to_text(pdf_file):
    text = ""

    pdf_reader = PdfReader(pdf_file)
    
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    return text

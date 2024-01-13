import PyPDF2

def pdf_to_text(pdf_path):
    text = ""

    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text

# Replace 'your_pdf_file.pdf' with the actual path to your PDF file
pdf_path = 'your_pdf_file.pdf'
result_text = pdf_to_text(pdf_path)

print(result_text)
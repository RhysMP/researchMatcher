from flask import Flask, request
import PyPDF2
import os

app = Flask(__name__)

def pdf_to_text(pdf_path):
    text = ""

    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text

@app.route('/uploadFile', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save('' + file.filename)

    # Replace 'your_pdf_file.pdf' with the actual path to your PDF file
    pdf_path = file.filename
    result_text = pdf_to_text(pdf_path)

    with open('output.txt', 'w') as output_file:
        output_file.write(result_text)

    # Delete the original PDF file
    os.remove(pdf_path)

    return 'File uploaded, converted to text, and saved successfully'

if __name__ == '__main__':
    app.run()


from flask import Flask, request, jsonify
from PyPDF2 import PdfReader
import os
import time

# import necessary packages


app = Flask(__name__)


def convert_pdf_to_text(pdf_file):
    text = ""

    pdf_reader = PdfReader(pdf_file)

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    return text
def test():
    result_text = convert_pdf_to_text("C:/Users/kingy/OneDrive/Desktop/SBHacks/sbhacksX/client/src/pages/Yasir_Whites_Resume-1.pdf")
    print(result_text)

@app.route('/uploadFile', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join("C:/Users/kingy/OneDrive/Desktop/SBHacks/sbhacksX/client/src/pages/", file.filename))
    major = request.form['major']
    name = request.form['name']

    # Replace 'your_pdf_[file.pdf' with the actual path to your PDF file
    result_text = convert_pdf_to_text("C:/Users/kingy/OneDrive/Desktop/SBHacks/sbhacksX/client/src/pages/" + file.filename)
    print(result_text)

    with open('output.txt', 'w') as output_file:
        output_file.write(result_text)

    # Delete the original PDF file
    response = jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200

if __name__ == '__main__':
    app.run()


 
# divison of labor: 
    
    


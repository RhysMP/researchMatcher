from flask import Flask, request
import PyPDF2
import os

# import necessary packages


app = Flask(__name__)

def pdf_to_text(pdf_path):
    text = ""

    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text


@app.route('/uploadFile', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join(os.getcwd(), file.filename))
    major = request.form['major']
    name = request.form['name']

    # formData.append('fileName', file.name);
    # formData.append('name', event.target.name.value);
    # formData.append('major', event.target.major.value);


    # Replace 'your_pdf_[file.pdf' with the actual path to your PDF file
    pdf_path = file.filename
    result_text = pdf_to_text(pdf_path)
    

    with open('output.txt', 'w') as output_file:
        output_file.write(result_text)

    # Delete the original PDF file
    os.remove(pdf_path)

    return result_text

if __name__ == '__main__':
    app.run()




 
# divison of labor: 
    
    


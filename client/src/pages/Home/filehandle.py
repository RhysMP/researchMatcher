from flask import Flask, request, jsonify
from PyPDF2 import PdfReader
import os
import requests
from keybert import KeyBERT
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

app = Flask(__name__)

def get_sim_score(student_keys, prof_keys):

    # extract keywords from tuples
    student_keys = [tup[0] for tup in student_keys]
    prof_keys = [tup[0] for tup in prof_keys]

    all_keys = student_keys + prof_keys
    
    # check if either set of keywords is empty
    if not student_keys or not prof_keys:
        return 0.01

    # create vectors for student and professor keywords
    vector_list1 = np.array([1 if key in student_keys else 0 for key in all_keys])
    vector_list2 = np.array([1 if key in prof_keys else 0 for key in all_keys])

    # calculate cosine similarity between the two vectors
    dot_product = np.dot(vector_list1, vector_list2)
    norm_product = np.linalg.norm(vector_list1) * np.linalg.norm(vector_list2)

    # calculate the overall similarity score
    sim_score = dot_product / norm_product if norm_product != 0 else 0.02 

    return sim_score






def get_student(stud_keys):

    # Specify the web address where the JSON data is hosted
    json_url = "https://d5e6-169-231-132-179.ngrok-free.app/professors"
    # Fetch JSON data from the web
    response_professors = requests.get(json_url)

    # Check if the request was successful (status code 200)
    if response_professors.status_code == 200:
        # Parse JSON data
        json_data = response_professors.json()

        # Check if "professors" key exists in the JSON data
        if "professors" in json_data:
            # Access the list of professors
            professors_list = json_data["professors"]
            # Iterate through the list of professors
            for professor in professors_list:
                profe_keys = professor['key_words']
                similarity_score = get_sim_score(stud_keys, profe_keys)
                professor['similarity_score'] = similarity_score 
                
            print(professors_list)
            return professors_list


        else:
            print("Error: 'professors' key not found in the JSON data")
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response_professors.status_code}")







def convert_pdf_to_text(pdf_file):
    text = ""

    pdf_reader = PdfReader(pdf_file)

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    return text


def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    similarity = intersection / union if union != 0 else 0
    return similarity







@app.route('/uploadFile', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join("/Users/kaankoc/Desktop/test/sbhacksX/client/src/pages/", file.filename))
    major = request.form['major']
    name = request.form['name']

    # Replace 'your_pdf_[file.pdf' with the actual path to your PDF file
    result_text = convert_pdf_to_text("/Users/kaankoc/Desktop/test/sbhacksX/client/src/pages/" + file.filename)

#    with open('output.txt', 'w') as output_file:
#        output_file.write(result_text)
    keywords = ["Blockchain technology", "software development", "Research", "Quantum", "Domain"]

   
    professor_list = get_student(keywords)


    response = jsonify({'professors': professor_list})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200

if __name__ == '__main__':
    app.run()


 
# divison of labor: 
    
    


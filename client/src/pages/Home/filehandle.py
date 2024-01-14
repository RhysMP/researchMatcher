from flask import Flask, request, jsonify
from PyPDF2 import PdfReader
import os
import requests
from keybert import KeyBERT
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
app = Flask(__name__)

# create function to use BERT model and extract keywords from students resume
def get_keywords_student(resume):
    # initialize BERT model 
    kw_model = KeyBERT(model="distilbert-base-nli-mean-tokens")

    # get keywords 
    keywords = kw_model.extract_keywords(resume, keyphrase_ngram_range=(1, 3), stop_words='english')

    # return keywords
    return keywords

# create function to use BERT model and extract keywords from profs description
def get_keywords_prof(research):
    # initialize BERT model 
    kw_model = KeyBERT(model="distilbert-base-nli-mean-tokens")

    # get keywords 
    keywords = kw_model.extract_keywords(research, keyphrase_ngram_range=(1, 2), stop_words='english')

    # return keywords
    return keywords


# function to get overall cosine similarity between both lists of keywords
def get_sim_score(student_keys, prof_keys):

    # extract keywords from tuples
    student_keys = [tup[0] for tup in student_keys]
    prof_keys = [tup[0] for tup in prof_keys]

    all_keys = student_keys + prof_keys
    
    
    # check if vocabulary is empty or contains only stop words
    if not any(word.isalpha() for word in all_keys):
        return 0.0  

    # create vectors for student and professor keywords
    vector_list1 = np.array([1 if key in student_keys else 0 for key in all_keys])
    vector_list2 = np.array([1 if key in prof_keys else 0 for key in all_keys])

    # calculate cosine similarity between the two vectors
    dot_product = np.dot(vector_list1, vector_list2)
    norm_product = np.linalg.norm(vector_list1) * np.linalg.norm(vector_list2)  # check this

    # calculate the overall similarity score
    sim_score = dot_product / norm_product if norm_product != 0 else 0.0  # this is causing 0.0

    return sim_score







def get_student(stud_keys):

    # Specify the web address where the JSON data is hosted
    json_url = "https://c049-169-231-132-179.ngrok-free.app/professors"
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









@app.route('/uploadFile', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join("C:/Users/kingy/OneDrive/Desktop/SBHacks/sbhacksX/client/src/pages/", file.filename))
    major = request.form['major']
    name = request.form['name']

    # Replace 'your_pdf_[file.pdf' with the actual path to your PDF file
    result_text = convert_pdf_to_text("C:/Users/kingy/OneDrive/Desktop/SBHacks/sbhacksX/client/src/pages/" + file.filename)

#    with open('output.txt', 'w') as output_file:
#        output_file.write(result_text)

    #keywords = get_keywords_student(result_text)
    keywords = ["future surgery", "new research", "new research"]
    print(keywords)
    professor_list = get_student(keywords)
    for professor in professor_list:
        print(professor["similarity_score"])

    response = jsonify({'professors': professor_list})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200

if __name__ == '__main__':
    app.run()


 
# divison of labor: 
    
    


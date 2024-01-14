import requests
import json
from final_sim_score import get_sim_score

def get_student(id):
    # Specify the web address where the JSON data is hosted
    json_url = "https://b826-169-231-132-179.ngrok-free.app/students/" + str(id)
    # Fetch JSON data from the web
    response_student = requests.get(json_url)
    data = response_student.json()
    studentJson = data["student"]
    stud_keys = studentJson['key_words']

    # Specify the web address where the JSON data is hosted
    json_url = "https://b826-169-231-132-179.ngrok-free.app/professors"
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
                print(professor)


        else:
            print("Error: 'professors' key not found in the JSON data")
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response_professors.status_code}")


import requests
import json
from final_sim_score import get_sim_score

def get_student(keywords):
    stud_keys = keywords['key_words']

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


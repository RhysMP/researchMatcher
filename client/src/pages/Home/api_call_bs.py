import requests
import json

# Specify the web address where the JSON data is hosted
json_url = "https://b826-169-231-132-179.ngrok-free.app/professors"
# Fetch JSON data from the web
response = requests.get(json_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse JSON string into a dictionary
    data = json.loads(response.text)

    # Specify the professor's ID you are interested in
    professor_id_to_find = 3

    # Find the professor with the specified ID
    selected_professor = next((professor for professor in data["professors"] if professor["id"] == professor_id_to_find), None)

    # Check if the professor was found
    if selected_professor:
        # Extract and store the keywords as a string
        keywords_string = ", ".join(selected_professor["key_words"])
        print("Keywords of Prof. Nathaniel:", keywords_string)
    else:
        print("Professor not found with ID:", professor_id_to_find)
else:
    print("Failed to fetch JSON data. Status code:", response.status_code)

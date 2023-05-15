import json
import requests

url = "https://rickandmortyapi.com/api/character/{id}"
id_value = "1"
formatted_url = url.format(id=id_value)

try:
    response = requests.get(formatted_url, timeout=5)
    if response.status_code == 200:
        try:
            data = json.loads(response.text)
            name = data['name']
            status = data['status']
            species = data['species']
            gender = data['gender']

            print(f"Name: {name} "
                  f"\nStatus: {status} "
                  f"\nSpecies: {species} "
                  f"\nGender: {gender}")

        except json.JSONDecodeError:
            print("Invalid JSON response received.")
    elif response.status_code == 404:
        print("Character not found.")
    elif response.status_code == 500:
        print("Internal Server Error.")
    else:
        print(f"Error: {response.status_code}")
except requests.RequestException as e:
    print(f"An error occurred: {e}")

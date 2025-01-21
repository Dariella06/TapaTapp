import requests
# https://nationalize.io/documentation
url = "https://api.nationalize.io/?name=nathaniel"
response = requests.get(url)
if response.status_code == 200:
    print("Contingut:", response.json())
else:
    print("Error:", response.status_code)
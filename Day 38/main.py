import requests
from datetime import datetime
from config import APP_ID, API_KEY, SHEETY_ENDPOINT, SHEETY_TOKEN

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

api_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

query = input("Which exercises did you do? ")
api_params = {
 "query": query,
 "gender": "male",
 "weight_kg": 65.0,
 "height_cm": 171.5,
 "age": 26
}

response = requests.post(api_endpoint, json=api_params, headers=api_headers)
result = response.json()
print(result)

sheet_api_endpoint = SHEETY_ENDPOINT

now = datetime.now()
# print(now.strftime("%d/%m/%Y"))
sheety_headers = {
    "Authorization": SHEETY_TOKEN
}
for exercise in result["exercises"]:
    sheety_params = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_api_endpoint, json=sheety_params, headers=sheety_headers)
    print(sheet_response.text)

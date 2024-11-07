import requests
from config import SHEETY_ENDPOINT, SHEETY_ENDPOINT_USERS

class DataManager:

    def __init__(self):
        self.prices_endpoint = SHEETY_ENDPOINT
        self.users_endpoint = SHEETY_ENDPOINT_USERS
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.prices_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                    "price": {"iataCode": city["iataCode"]}
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint)
        data = response.json()
        # See how Sheet data is formatted so that you use the correct column name!
        # pprint(data)
        # Name of spreadsheet 'tab' with the customer emails should be "users".
        self.customer_data = data["users"]
        return self.customer_data
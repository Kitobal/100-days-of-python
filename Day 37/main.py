import requests
from datetime import datetime
from config import api_token

USERNAME = "kitobal"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

# --create pixela user-- #

user_params = {
    "token": api_token,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# --create graph-- #
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Minutes of Study",
    "unit": "Minutes",
    "type": "int",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": api_token
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)


# --post a pixel--#
pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15",
}
# response = requests.post(url=pixel_post_endpoint, json=pixel_post_params, headers=headers)
# print(response.text)

# --update a pixel-- #
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixel_update_params = {
    "quantity": "20"
}

response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=headers)
print(response.text)

# --delete a pixel-- #
delete_pixel_endpoint = pixel_update_endpoint

# response = requests.delete(url=pixel_update_endpoint, headers=headers)
# print(response.text)
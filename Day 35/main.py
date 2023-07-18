import requests
import smtplib
from config import api_key, my_email, my_password, to_email

# Lat Long Viña del Mar, Chile
LATITUDE = -33.1
LONGITUDE = -71.33

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

for hour in range(0, 12):
    weather_id = weather_data["hourly"][hour]["weather"][0]["id"]
    if weather_id < 600:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=to_email,
                                msg="Subject: Will Rain Today\n\nBring an Umbrella")
        break

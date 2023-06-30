# DAY 35 Project: Rain Check!

import os
import requests
from twilio.rest import Client

twilio_account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

owm_api_key = os.environ.get("OWM_API_KEY")

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# NYC coordinates
parameters = {
    "lat": 40.7143,
    "lon": -74.006,
    "appid": owm_api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
print(f"API status code response: {response.status_code}")

weather_data = response.json()
hourly_data = weather_data["hourly"]
first_twelve_hours = hourly_data[0:12]

will_rain = False

for hour_data in first_twelve_hours:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True


twilio_number = os.environ.get("TWILIO_NUMBER")
my_number = os.environ.get("MY_NUMBER")

if will_rain:
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        from_=twilio_number,
        to=my_number,
        body='It is going to rain today. Remember to bring an umbrella! ⛱'
    )
    print(message.status)

# DAY 38 Project: FitTrack

import os
import requests
import json
import datetime

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
NUTRITION_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ['SHEETY_ENDPOINT']
TOKEN = os.environ['TOKEN']

# Required HEADERS when accessing Nutritionix V2 API endpoints: x-app-id: Your app ID issued from
# developer.nutritionix.com) x-app-key: Your app key issued from developer.nutritionix.com) x-remote-user-id:  A
# unique identifier to represent the end-user who is accessing the Nutritionix API.
#
# Please note, when authenticating with the API, you must send the x-app-id and x-app-key params as headers,
# and not as query string parameters.

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
    "x-remote-user-id": "0",
}

exercise_text = input("Tell me which exercises you did: ")
payload = json.dumps({
    "query": exercise_text,
})
response = requests.post(url=NUTRITION_ENDPOINT, headers=headers, data=payload)
response.raise_for_status()

# response.json(): This method tries to parse the response content as JSON and returns the parsed JSON data as a
# Python dictionary or list. It is useful for handling JSON responses.

data = response.json()
data = data['exercises'][0]
activity = (data['name']).title()
duration = data['duration_min']
calories = round(data['nf_calories'])

# Using the Sheety Documentation, write some code to use the Sheety API to generate a new row of data in your
# Google Sheet for each of the exercises that you get back from the Nutritionix API. The date and time columns should
# contain the current date and time from the Python datetime module.

current_datetime = datetime.datetime.now()
current_time = current_datetime.strftime("%I:%M:%S")
current_date = current_datetime.strftime("%d/%m/%Y")

body = {
    "workout": {
        "date": current_date,
        "time": current_time,
        "exercise": activity,
        "duration": duration,
        "calories": calories,
    }
}

# Using the Sheety documentation on authentication to update your Python code to authenticate your request by adding
# a "Bearer Token" to your Sheety endpoint.

headers = {
    "Authorization": TOKEN,
}
response = requests.post(url=SHEETY_ENDPOINT, json=body, headers=headers)
response.raise_for_status()
print("Metrics have been logged to your workout spreadsheets.")

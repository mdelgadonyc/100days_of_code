# DAY 37 Project: Habitual

import requests
import os
import datetime

TOKEN = os.environ['API_KEY']
USERNAME = os.environ['USERNAME']
GRAPH_ID = os.environ['GRAPH_ID']
PIXELA_ENDPOINT = f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}'

#todayDate = datetime.datetime.today().strftime("%Y%m%d")
todayDate = datetime.date(2023, 7, 11).strftime("%Y%m%d")
print (todayDate)

parameters = {
#    "date": todayDate,
    "quantity": "2",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
putUrl = f'{PIXELA_ENDPOINT}/{todayDate}'
# response = requests.post(PIXELA_ENDPOINT, json=parameters, headers=headers)
# response = requests.post(url=deleteUrl, headers=headers)
response = requests.put(url=putUrl, json=parameters, headers=headers)

print(response.text)

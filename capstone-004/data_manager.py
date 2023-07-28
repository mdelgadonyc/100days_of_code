import os
import requests
import json

SHEETY_ENDPOINT = os.environ.get('ENV_SHEETY_ENDPOINT')
SHEETY_TOKEN = os.environ.get('ENV_SHEETY_TOKEN')


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def set_iata(code, row_num):
        """
        Sets the IATA code field for a row in the Google Sheet via Sheety API.
        """

        url = SHEETY_ENDPOINT+"/"+row_num

        payload = json.dumps({
            "price": {
                "iataCode": code
            }
        })

        headers = {
            'Content-Type': 'application/json',
            'Authorization': SHEETY_TOKEN
        }

        response = requests.put(url=url, headers=headers, data=payload)


    def get_rows():
        """
        Retrieves all rows from Google Sheet via Sheety API.

        Returns:
            All data rows.

        Example:
            >>> get_rows()
            {'prices': [{'city': 'Mumbai', 'iataCode': '', 'lowestPrice': 2000, 'id': 2},
                           {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 2000, 'id': 3},
            }
        """
        headers = {
            "Authorization": SHEETY_TOKEN
        }

        response = requests.get(url=SHEETY_ENDPOINT, json=headers)
        response.raise_for_status()
        data = response.json()

        # hard coded values to reduce API calls while debugging
        # data = {'prices': [{'city': 'Mumbai', 'iataCode': 'BOM', 'lowestPrice': 5, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 2000, 'id': 3}, {'city': 'Beijing', 'iataCode': 'BJS', 'lowestPrice': 485, 'id': 4}, {'city': 'Shanghai', 'iataCode': 'SHA', 'lowestPrice': 551, 'id': 5}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 95, 'id': 6}, {'city': 'Chicago', 'iataCode': 'CHI', 'lowestPrice': 414, 'id': 7}, {'city': 'Los Angeles', 'iataCode': 'LAX', 'lowestPrice': 240, 'id': 8}]}

        rows = data['prices']

        return rows

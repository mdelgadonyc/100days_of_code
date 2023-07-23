import os
import requests

SHEETY_ENDPOINT = os.environ.get('ENV_SHEETY_ENDPOINT')
SHEETY_TOKEN = os.environ.get('ENV_SHEETY_TOKEN')


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def get_cities():
        """
        Retrieves all cities from Google Sheet via Sheety API.

        Returns:
            List of cities.

        Example:
            >>> get_cities()
            ['Mumbai', 'Berlin']
        """
        headers = {
            "Authorization": SHEETY_TOKEN
        }

        # response = requests.get(url=SHEETY_ENDPOINT, json=headers)
        # response.raise_for_status()

        # data = response.json()
        # hard coded values to reduce API calls while debugging
        data = {'prices': [{'city': 'Mumbai', 'iataCode': '', 'lowestPrice': 2000, 'id': 2},
                           {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 2000, 'id': 3},
                           {'city': 'Beijing', 'iataCode': '', 'lowestPrice': 2000, 'id': 4},
                           {'city': 'Shanghai', 'iataCode': '', 'lowestPrice': 2000, 'id': 5},
                           {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 2000, 'id': 6},
                           {'city': 'Chicago', 'iataCode': '', 'lowestPrice': 2000, 'id': 7},
                           {'city': 'Los Angeles', 'iataCode': '', 'lowestPrice': 2000, 'id': 8}]}

        rows = data['prices']

        cities = []

        for row in rows:
            cities.append(row['city'])

        return cities

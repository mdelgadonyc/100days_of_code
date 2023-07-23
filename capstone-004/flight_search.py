import os

import requests
import os

FLIGHT_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
FLIGHT_APIKEY = os.environ.get('ENV_FLIGHT_APIKEY')

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_code(city_name):
        """
        Retrieve an IATA code for the given city name

        Returns:
            IATA code as a string
        """

        parameters = {
            "term": city_name,
        }

        headers = {
            "apikey": FLIGHT_APIKEY
        }
        response = requests.get(url=FLIGHT_ENDPOINT, params=parameters, headers=headers)
        response.raise_for_status()

        data = response.json()
        data = data['locations'][0]
        iata_code = data['code']

        return iata_code

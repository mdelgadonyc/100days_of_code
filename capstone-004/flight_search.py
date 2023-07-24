import os

import requests
import os

FLIGHT_ENDPOINT = "https://api.tequila.kiwi.com"
FLIGHT_APIKEY = os.environ.get('ENV_FLIGHT_APIKEY')

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_flight(code):
        """
        Retrieve cheapest flight for the given city from NYC within the next 6 months.

        Returns:
            ??? as a string
        """


        parameters = {
            "fly_from": "NYC",
            "fly_to": code,
            "date_from": "24/07/2023",
            "date_to": "24/01/2024",
            "one_for_city": "1",
            "curr": "USD"
        }

        headers = {
            "apikey": FLIGHT_APIKEY
        }

        search_endpoint_url = FLIGHT_ENDPOINT + "/v2/search"

        response = requests.get(url=search_endpoint_url, params=parameters, headers=headers)
        response.raise_for_status()

        data = response.json()
        data = data['data'][0]
        price = f"${data['price']}"
        print(price)


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

        location_endpoint_url = FLIGHT_ENDPOINT+"/locations/query"

        response = requests.get(url=location_endpoint_url, params=parameters, headers=headers)
        response.raise_for_status()

        data = response.json()
        data = data['locations'][0]
        iata_code = data['code']

        return iata_code

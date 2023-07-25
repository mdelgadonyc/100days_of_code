# DAY 39 Project: [Capstone] Take Flight!
#
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
#
# Program Requirements
#
# ✅️ Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport
# Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the
# city code (not the airport code see here).
#
# ✅️ Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
#
# ✅️ If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.
#
# ✅️ The SMS should include the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates. e.g.

import data_manager
import flight_search
import notification_manager

manager = data_manager.DataManager
print(manager.get_rows())

flight = flight_search.FlightSearch()

rows = manager.get_rows()

for row in rows:
    # Populate your copy of the Google Sheet with International Air Transport Association (IATA) codes for each city
    if row['iataCode'] == '':
        row_num = str(row['id'])
        code = flight.get_code(row['city'])
        print(f'{code} {row_num}')
        manager.set_iata(code, row_num)
    else:
        code = row['iataCode']
        print(f"Existing IATA code found for {row['city']}, skipping...")
    flight_manager = flight.get_flight(code)

    # Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in
    # the Google Sheet.

    price = flight_manager.get_price()
    print(price)
    if price < row['lowestPrice']:
        print('ok')
        destination_code = flight_manager.get_destination_code()
        departure_code = flight_manager.get_departure_code()
        link = flight_manager.get_link()
        departure_date = flight_manager.get_date()
        message_txt = f"Hi! Found a deal from {departure_code} in NYC to {destination_code} in {row['city']} on " \
                      f"{departure_date} for ${price}! Click on this look to book now: {link}"

        messenger = notification_manager.NotificationManager()
        messenger.send_message(message_txt)







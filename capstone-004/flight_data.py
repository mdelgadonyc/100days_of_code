class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.link = None
        self.price = int
        self.departure_code = None
        self.destination_code = None
        self.date = None

    def set_data(self, data):
        self.link = data['deep_link']
        self.price = data['price']
        self.departure_code = data['flyFrom']
        self.destination_code = data['flyHome']
        self.date = data['local_departure']

    def get_price(self):
        return self.price

    def get_link(self):
        return self.link

    def get_departure_code(self):
        return self.departure_code

    def get_destination_code(self):
        return self.destination_code

    def get_date(self):
        return self.date

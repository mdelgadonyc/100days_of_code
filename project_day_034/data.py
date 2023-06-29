# Modify the data.py file (don't change the main.py)
# Make a get() request to fetch 10 True or False questions.
# Parse the JSON response and replace the value of question_data (don't change the variable name)
# Hint: create a Python dictionary for the amount and type parameters.None

import requests

parameters = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
data = response.json()
question_data = data["results"]
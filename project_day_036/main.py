# DAY 36 Project: Ticker Tracker

import os
import requests
import datetime
import twilio.rest

STOCK_NAME = "AAPL"
COMPANY_NAME = "Apple"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# STEP 1: Use https://www.alphavantage.co/documentation/#dailyadj [NOTE: #daily is now premium only]
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
#  e.g. [new_value for (key, value) in dictionary.items()]

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": os.environ["ALPHA_APIKEY"],
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

# today_date = str(datetime.datetime.now()).split(" ")[0]
today_date = str(datetime.datetime.today()).split(" ")[0]
# today_date = str(datetime.datetime.today() - datetime.timedelta(days=3)).split(" ")[0]

today_stock_data = data['Time Series (Daily)'][today_date]
today_stock_price = float(today_stock_data['4. close'])

# Get the day before yesterday's closing stock price
yesterday_date = str(datetime.datetime.today() - datetime.timedelta(days=1)).split(" ")[0]
yesterday_stock_data = data['Time Series (Daily)'][yesterday_date]
yesterday_stock_price = float(yesterday_stock_data['4. close'])

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint:
# https://www.w3schools.com/python/ref_func_abs.asp
price_difference = abs(today_stock_price - yesterday_stock_price)
arrow = '🔺' if (today_stock_price > yesterday_stock_price) else '🔻'

# Work out the percentage difference in price between closing price yesterday and closing price the day before
# yesterday.
percentage = price_difference / yesterday_stock_price
print(f"Stock price percentage difference is {(percentage * 100):.2f}% {arrow}")

# If percentage is greater than 5 then use the News API to get the first 3 news articles related to the COMPANY_NAME.
# STEP 2: https://newsapi.org/

if percentage > 0.05:
    parameters = {
        "q": COMPANY_NAME,
        # "pageSize": 3,
        "sortBy": "publishedAt",
        "searchIn": "title",
        "language": "en",
        "apiKey": os.environ["NEWS_APIKEY"]
    }
    response = requests.get(NEWS_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()

    # Use Python slice operator to create a list that contains the first 3 articles.
    three_articles = data['articles'][0:3]

    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # Create a new list of the first 3 article's headline and description using list comprehension.
    article_list = [(article['title'], article['description']) for article in three_articles]

    # Send each article as a separate message via Twilio.

    twilio_acct_id = os.environ['TWILIO_ACCT_ID']
    twilio_auth_token = os.environ['TWILIO_AUTH_KEY']
    client = twilio.rest.Client(twilio_acct_id, twilio_auth_token)

    for article_title, article_description in article_list:
        article_formatted = f"""
            {STOCK_NAME}: {arrow}{(percentage * 100):.2f}%
            Headline: {article_title} ({STOCK_NAME}). 
            Brief: {article_description}
            """
        message = client.messages.create(
            from_=os.environ['TWILIO_NUMBER'],
            body=article_formatted,
            to=os.environ['MY_SMS_NUMBER']
        )

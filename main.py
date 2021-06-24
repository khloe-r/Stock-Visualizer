# Import libraries to handle HTTP requests
import requests
import json
# Use Secrets
import os
TOKEN = os.environ['FINNHUB_API_KEY'] #Secret Environment Variable

header = {'X-Finnhub-Token': TOKEN}
r = requests.get(f'https://finnhub.io/api/v1/quote?symbol=AAPL', headers = header)

#print(r.content)
# c - current price
# h - highest price of day
# l - lowest price of day
# o - opening price
# pc - close price (previous day)
# t - timestamp

dictionary = json.loads(r.content)
# Import libraries to handle HTTP requests
import requests
import json
# Use Secrets
import os
TOKEN = os.environ['FINNHUB_API_KEY'] #Secret Environment Variable

# Asks user for Stock to search
line = input("Give me a stock symbol? ")

# Makes request to the API
header = {'X-Finnhub-Token': TOKEN}
r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={line}', headers = header)

#print(r.content)
# c - current price
# h - highest price of day
# l - lowest price of day
# o - opening price
# pc - close price (previous day)
# t - timestamp

# Converts Response data type to a python dictionary
pydict = json.loads(r.content)

# Calculate percent change since day prior
value = pydict['c']
previousClose = pydict['pc']
percentChange = ((value - previousClose)/previousClose) * 100

# Output desired information
print(line + ':')
print("\t Current Value", "$" + str(value), sep = " - ")
print("\t Previous Close", "$" + str(previousClose), sep = " - ")
print("\t Percent Change", "{:.3f}".format(percentChange)+"%", sep = " - ")
# Import libraries to handle HTTP requests
import requests
import json
from datetime import date, datetime
# Import libraries for data visualization
import matplotlib.pyplot as plt
# Use Secrets for API token
import os
TOKEN = os.environ['FINNHUB_API_KEY'] #Secret Environment Variable

# Asks user for Stock to search
line = input("Give me a stock symbol? ")

# Find current date for company news
today = str(date.today())
year = today[:4]
month = today[5:7]
startmonth = int(month) - 3
if startmonth < 1:
  startmonth = 12 - startmonth
day = today[8:]

# Makes request to the API
header = {'X-Finnhub-Token': TOKEN}
stock = requests.get(f'https://finnhub.io/api/v1/quote?symbol={line}', headers = header)
company = requests.get(f'https://finnhub.io/api/v1/stock/profile2?symbol={line}', headers = header)
companyNews = requests.get(f'https://finnhub.io/api/v1/company-news?symbol={line}&from={year}-{str(startmonth)}-{day}&to={year}-{month}-{day}', headers = header)

#print(stock.content)
# c - current price
# h - highest price of day
# l - lowest price of day
# o - opening price
# pc - close price (previous day)
# t - timestamp

# Converts Response data type to a python dictionary
stockdict = json.loads(stock.content)
companydict = json.loads(company.content)
newsdict = json.loads(companyNews.content)

# Calculate percent change since day prior
value = stockdict['c']
highestValue = stockdict['h']
lowestValue = stockdict['l']
previousClose = stockdict['pc']
percentChange = ((value - previousClose)/previousClose) * 100
companyName = companydict['name']

# Output visualization
x=['Highest of the Day','Lowest of the Day','Current']
y=[highestValue, lowestValue, value]
plt.ylim(lowestValue-1, highestValue+1)
plt.bar(x,y)
plt.show()

# Output desired information
print(companyName + f' ({line})' + ':')
print("\t Current Value", "$" + str(value), sep = " - ")
print("\t Previous Close", "$" + str(previousClose), sep = " - ")
print("\t Percent Change", "{:.3f}".format(percentChange)+"%", sep = " - ")

# Prints Latest News
print(f'\nLatest News About {companyName}:')
for i in newsdict[:3]:
  # Formats Date of News Story
  timestamp = int(i['datetime'])
  timestamp = datetime.utcfromtimestamp(timestamp).strftime('%b %d, %Y')

  print(f"{timestamp}\n{i['headline']}\n{i['summary']} - {i['source']}\n")
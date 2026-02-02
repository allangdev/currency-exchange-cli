# import library

import requests
from datetime import datetime

datetime.fromtimestamp(1740780008)
# URL without API key
url_api = "https://economia.awesomeapi.com.br/"

# message for failed search
result_failed = "MOEDA NOT FOUND ❌❌❌"

# create function 
def search_coin_temp_real(coin_name):
  search = requests.get( url_api + 'last/' + coin_name.upper())
  # check if exist or not 
  if search.status_code == 404:
    return result_failed
  # return json data modify
  data = search.json()
  name = data[next(iter(data))]['name']
  code = data[next(iter(data))]['code']
  codein = data[next(iter(data))]['codein']
  high = data[next(iter(data))]['high']
  low = data[next(iter(data))]['low']
  varbid = data[next(iter(data))]['varBid']
  bid = data[next(iter(data))]['bid']
  ask = data[next(iter(data))]['ask']
  pctChange = data[next(iter(data))]['pctChange']
  timestamp = datetime.fromtimestamp(int(data[next(iter(data))]['timestamp']))

  # create success message
  result_sucess = f"""
The currency exchange data you requested was found successfully. ✅

Here are the details for the {name} exchange rate:

Currency Pair: {name}
Base Currency: {code}
Target Currency: {codein}

📊 Market Data:

Current Buy Price (Bid): {bid} 
Current Sell Price (Ask): {ask}
Highest Rate of the Day: {high} 
Lowest Rate of the Day: {low} 

📉 Price Variation:

Absolute Change: {float(varbid)}
Percentage Change: {float(pctChange)}%

🕒 Last Update:

Date and Time: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}
          """
  return result_sucess

def search_coin_last_days(coin_name, date_start, date_end):
  search = requests.get(url_api + 'json/daily/' + coin_name.upper() + '/' + '?start_date='+ date_start + '&end_date=' + date_end)
  # check if exist or not 
  if search.status_code == 404:
    return result_failed
  # try or except for date format
  try:
    # return json data modify
    data = search.json()
    name = data[0]['name']
    code = data[0]['code']
    codein = data[0]['codein']
    high = data[0]['high']
    low = data[0]['low']
    varbid = data[0]['varBid']
    bid = data[0]['bid']
    ask = data[0]['ask']
    pctChange = data[0]['pctChange']
    timestamp = datetime.fromtimestamp(int(data[0]['timestamp']))

    # create success message
    result_sucess = f"""
  The currency exchange data you requested was found successfully. ✅

  Here are the details for the {name} exchange rate:

  Currency Pair: {name}
  Base Currency: {code}
  Target Currency: {codein}

  📊 Market Data:

  Current Buy Price (Bid): {bid} 
  Current Sell Price (Ask): {ask}
  Highest Rate of the Day: {high} 
  Lowest Rate of the Day: {low} 

  📉 Price Variation:

  Absolute Change: {float(varbid)}
  Percentage Change: {float(pctChange)}%

  🕒 Last Update:

  Date and Time: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}
            """
    return result_sucess
  except:
    return "Invalid date format. Please use YYYY/MM/DD ❌❌❌"

# function to start the program
def start():
  print("Welcome to the Currency Exchange Rate Search System! 🌍💱")
  coin = input("Please enter the currency abbreviation you want to search (e.g., USD-BRL for USD to BRL): ")
  date_start = input("Please enter the START date for historical data (YYYY/MM/DD) or leave blank for current data: ")
  date_end = input("Please enter the END date for historical data (YYYY/MM/DD) or leave blank for current data: ")
  if date_start and date_end:
    result = search_coin_last_days(coin, date_start, date_end)
  else:
    result = search_coin_temp_real(coin)
  
  print(result)

start()
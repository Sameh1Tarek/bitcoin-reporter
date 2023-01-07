import requests
import time

#global variables
api_key= 'your api key on CoinMarketCap website'
bot_key= 'your new telegram bot key'
chat_id= 'your chat_id in telegram'
#limit of price you need
limit=59000
time_interval=5

#to get price from CoinMarketCap website
def get_price():
    #url,parameters and headers from API Documentation
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    #to limit data you want to recover it from CoinMarketCap website
    parameters = {
        'start': '1',
        'limit': '2',
        'convert': 'USD'
    }

    #way to talk CoinMarketCap website
    headers = {
          'Accepts': 'application/json',
          'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
    }
    respose = requests.get(url, headers=headers,params=parameters).json()
    btc_price=respose['data'][0]['quote']['USD']['price']
    #json is format of API data
    return btc_price

#to send price in telegram from bot
def send_update(chat_id,msg):
    url= f'https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}'
    requests.get(url)

def main():
    while True:
        price = get_price()
        print(price)
        if price<limit:
         send_update(chat_id,f"hello bro bitcoin price :{price}")
        #Repeat every five second
        time.sleep(time_interval)

main()

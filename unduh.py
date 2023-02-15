import requests
import json
import time

# set up the request parameters
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'your-api-key'
}
parameters = {
    'symbol': 'BTC',
    'convert': 'IDR'
}

# make a request to the API every 10 seconds and print the Bitcoin price
while True:
    response = requests.get(url, headers=headers, params=parameters)
    if response.status_code == 200:
        data = response.json()
        btc_price = data['data']['BTC']['quote']['IDR']['price']
        print(f'Harga Bitcoin saat ini adalah: {btc_price} IDR')
    else:
        print('Gagal mengambil data API')
    time.sleep(10)  # wait for 10 seconds before making the next request
	 
        

    

    


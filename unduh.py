import requests
import time

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '7152156b-9a3a-452f-8970-d6559e95c368'
}
parameters = {
  'symbol': 'BTC',
  'convert': 'IDR'
}
while True:
response = requests.get(url, headers=headers, params=parameters)
if response.status_code == 200:
    data = response.json()
    btc_price = data['data']['BTC']['quote']['IDR']['price']
    print(f'Harga Bitcoin saat ini adalah: {btc_price} IDR')
else:
    print('Gagal mengambil data API')

time.sleep(120)
	 
        

    

    


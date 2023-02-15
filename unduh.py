import requests
import time

while True:
    # URL endpoint untuk mengunduh data pasar kripto dari CoinMarketCap
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    # Tambahkan parameter API key ke header permintaan
    headers = {
     "X-CMC_PRO_API_KEY": "7152156b-9a3a-452f-8970-d6559e95c368"
    }

    parameters = { 'symbol': 'BTC', 'convert': 'IDR' }
 response = requests.get(url, headers=headers, params=parameters) if response.status_code == 200: data = response.json() btc_price = data['data']['BTC']['quote']['IDR']['price'] print(f'Harga Bitcoin saat ini adalah: {btc_price} IDR') else: print('Gagal mengambil data API')

    # Tunggu selama setengah jam sebelum mengambil data lagi
    time.sleep(120)



        

    

    


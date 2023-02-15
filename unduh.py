import requests
import json
import time
import mysql.connector

# set up the request parameters
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '7152156b-9a3a-452f-8970-d6559e95c368'
}
parameters = {
    'symbol': 'BTC',
    'convert': 'none'
}

# connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dataapicoinmarketcap"
)

# define function to get current timestamp
def last_updated():
    return int(time.time())

# make a request to the API every 5 minutes and save the Bitcoin price to the database
while True:
    response = requests.get(url, headers=headers, params=parameters)
    if response.status_code == 200:
        data = response.json()
        btc_price = data['data']['BTC']['quote']['USD']['price']
        print(f'Harga Bitcoin saat ini adalah: {btc_price} USD')

        # save the Bitcoin price to the database
        mycursor = mydb.cursor()
        sql = "INSERT INTO bitcoin_prices (price, last_updated) VALUES (%s, %s)"
        val = (btc_price, last_updated())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    else:
        print('Gagal mengambil data API')
    time.sleep(300)  # wait for 5 minutes before making the next request

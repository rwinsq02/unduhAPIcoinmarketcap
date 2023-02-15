import requests
import json
import time
import mysql.connector import Error
from datetime import datetime

# set up the request parameters
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '7152156b-9a3a-452f-8970-d6559e95c368'
}
parameters = {
    'symbol': 'BTC',
    
}

# connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dataapicoinmarketcap"
)
      mycursor = mydb.cursor()
# make a request to the API every 6 minute and save the Bitcoin price to the database
while True:
    try:
    response = requests.get(url, headers=headers, params=parameters)
if response.status_code == 200:
    data = response.json()
    btc_price = data['data']['BTC']['quote']['BTC']['price']
    last_updated = data['data']['BTC']['quote']['BTC']['last_updated']
    print(f"Nilai Bitcoin saat ini: {btc_price} ")
    print(f"Waktu terakhir diperbarui: {datetime.fromisoformat(last_updated).strftime('%Y-%m-%d %H:%M:%S')}")
    
    print("Gagal memuat data nilai Bitcoin")
        # save the Bitcoin price to the database
         sql = "INSERT INTO btc_price (price, last_updated) VALUES (%s, %s)"
    val = (btc_price, last_updated)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
   except Error as e:
        print('Gagal mengambil data API')
        finally:
    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()
        print("MySQL connection is closed")
    time.sleep(360)  # wait for 6 minutes before making the next request
        

    

    


import requests
import mysql.connector
from mysql.connector import Error
import time

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

headers = {

    "Accepts": "application/json",

    "X-CMC_PRO_API_KEY": "7152156b-9a3a-452f-8970-d6559e95c368"

}

parameters = {

    "symbol": "BTC",

    "convert": "none"

}

# Connect to the database

try:

    mydb = mysql.connector.connect(

        host="localhost",

        user="root",

        password="",

        database="dataapicoinmarketcap"

    )

    mycursor = mydb.cursor()

    # Insert data into the table

    sql = "INSERT INTO bitcoin_prices (price, last_updated) VALUES (%s, %s)"

    

    while True:

        # Get the Bitcoin data from the API

        response = requests.get(url, headers=headers, params=parameters)

        if response.status_code == 200:

            data = response.json()

            btc_price = data['data']['BTC']['quote']['USD']['price']

            last_updated = data['data']['BTC']['quote']['USD']['last_updated']

            print("Price of BTC is:", btc_price, "Last updated:", last_updated)

            val = (btc_price, last_updated)

            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")

        time.sleep(300) # Wait for 5 minutes

except Error as e:

    print("Error while connecting to MySQL", e)

finally:

    if (mydb.is_connected()):

        mycursor.close()

        mydb.close()

        print("MySQL connection is closed")



    

    


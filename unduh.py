import requests

import time

while True:

    # URL endpoint untuk mengunduh data pasar kripto dari CoinMarketCap

    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    # Tambahkan parameter API key ke header permintaan

    headers = {

        "X-CMC_PRO_API_KEY": "7152156b-9a3a-452f-8970-d6559e95c368"

    }

    # Lakukan permintaan API

    response = requests.get(url, headers=headers)

    # Periksa apakah permintaan berhasil dilakukan

    if response.status_code == 200:

        data = response.json()

        # Lakukan operasi yang ingin dilakukan dengan data

        print(data)

    else:

        print("Gagal mengambil data API dari CoinMarketCap")

    # Tunggu selama setengah jam sebelum mengambil data lagi

    time.sleep(1800)


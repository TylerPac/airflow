# fetch_crypto.py

import requests
import json
from datetime import datetime, timezone

def fetch_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin,ethereum',
        'vs_currencies': 'usd'
    }

    response = requests.get(url, params=params)
    data = response.json()

    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H-%M-%SZ')
    filename = f"crypto_prices_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    print(f"[{timestamp}] Saved prices to {filename}: {data}")

if __name__ == "__main__":
    fetch_prices()

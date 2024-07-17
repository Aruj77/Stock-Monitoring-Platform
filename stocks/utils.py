import requests


def fetch_stock_data(symbol: str) -> dict:
    api_key = "ZAUT54ES3OC2UN27" 
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=ibm&interval=5min&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

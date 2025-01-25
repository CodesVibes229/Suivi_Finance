import requests

def get_exchange_rate(base, target):
    url = f"https://api.exchangeratesapi.io/latest?base={base}"
    response = requests.get(url)
    data = response.json()
    return data['rates'].get(target, 1)

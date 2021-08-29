import requests

response = requests.get(
    'https://api.binance.com/api/v3/exchangeInfo',
)

# View the new `text-matches` array which provides information
# about your search term within the results
json_response = response.json()
symbols = [node["symbol"] for node in json_response['symbols']]
#symbols = [x for x in symbols if x.endswith('USDT')]
print(len(symbols))
print(symbols[:10])
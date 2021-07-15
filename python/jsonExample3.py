import requests
url = 'https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page=1&pageSize=20'
response = requests.get(url).json()
print(response)
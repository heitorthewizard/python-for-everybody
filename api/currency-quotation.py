import requests

currency = 'USD-BRL'

url = f'https://economia.awesomeapi.com.br/last/{currency}'
request = requests.get(url)
print('Retrieving', url)
data = request.json()
print('Retrieved', url)
bid_price = data['USDBRL']['bid']
print('To buy a USD $1 with you need BRL R${:.2f}'.format(float(bid_price)))


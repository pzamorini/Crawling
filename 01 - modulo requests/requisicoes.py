import requests

response = requests.get('https://www.nba.com/schedule')

print('Status Code:', response.status_code)
print('Headers:', response.headers)
print('\n Content:', response.content)
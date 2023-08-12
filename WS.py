import requests

url = 'https://www.wikipedia.org/'
response = requests.get(url)
print(dir(response))
# print(response.text)
# print(response.headers)

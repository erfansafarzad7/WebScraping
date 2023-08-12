import requests

"""
L 1
"""
# url = 'https://www.wikipedia.org/'
# response = requests.get(url)
# print(dir(response))
# # print(response.text)
# # print(response.headers)

# ------------------------------------------------------
"""
L2
"""
from bs4 import BeautifulSoup
# import re
#
# url = 'https://en.wikipedia.org/wiki/Mao_Zedong'
# response = requests.get(url)
#
# content = BeautifulSoup(response.text, 'html.parser')   #use python parser

# print(content.find('h2'))
# print(content.find('h2').text)
# print(content.find('h2').attrs)
# print(content.find('h2').get('id'))
# print(content.find(attrs={'class_': 'mw-indicator'}))  #Using class as a keyword argument will give you a syntax error
# print(content.find('a', class_='mw-indicator'))
# print(content.find(re.compile('^l')))

# print(content.find_all('h2'))
# print(content.find_all('h2', limit=5))
# print(content.find_all(['h1', 'h2']))

# print(content.select('li > a[title="Benjamin Tucker"]'))    #css selectors
# print(content.select('html head title'))
# print(content.select('p:nth-of-type(3)'))
# print(content.select('div > label'))

# ------------------------------------------------------

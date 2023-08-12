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
import re
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
"""
L 3
"""

url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'
response = requests.get(url)
content = BeautifulSoup(response.text, 'html.parser')

episodes = []
ep_tables = content.select('table.wikiepisodetable')

for table in ep_tables:
    headers = []
    rows = table.find_all('tr')

    for header in table.find('tr').find_all('th'):
        headers.append(header.text)

    for row in table.find_all('tr')[1:]:
        values = []

        for col in row.find_all(['th', 'td']):
            values.append(col.text)

        if values:
            episode_dict = {headers[i]:values[i] for i in range(len(values))}
            episodes.append(episode_dict)

for ep in episodes:
    print(ep)

# ------------------------------------------------------
"""
L 4
"""

url = 'https://news.ycombinator.com/news'
req = requests.get(url)
content = BeautifulSoup(req.text, 'html.parser')

articles = []

for item in content.find_all('tr', class_='athing'):
    item_a = item.find('a')
    item_link = item_a.get('href') if item.a else None
    item_text = item_a.get_text(strip=True) if item_a else None
    next_row = item.find_next_sibling('tr')
    item_scores = next_row.find('span', class_='score')
    item_scores = item_scores.get_text(strip=True) if item_scores else '0 point'
    item_comments = next_row.find('a', text=re.compile('\d+(&nbsp;|\s)comment(s?)'))
    item_comments = item_comments.get_text(strip=True).replace('\xa0', ' ') if item_comments else '0 comment'

    articles.append({
        'link': item_link,
        'title': item_text,
        'score': item_scores,
        'comments': item_comments,
    })

for article in articles:
    print(article)

# ------------------------------------------------------

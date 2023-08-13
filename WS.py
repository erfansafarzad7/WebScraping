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
    item_a = item.find('a', href=re.compile('https'))
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
"""
L5
"""

url = 'https://github.com/{}'
username = 'erfansafarzad7'

req = requests.get(url.format(username), params={'tab': 'repositories'})
content = BeautifulSoup(req.text, 'html.parser')
repos_elements = content.find(id='user-repositories-list')
repos = repos_elements.find_all('li')

for repo in repos:
    name = repo.find('h3').find('a').get_text(strip=True)
    language = repo.find(attrs={'itemprop': 'programmingLanguage'})
    language = language.get_text(strip=True) if language else 'unknown'
    stars = repo.find('a', attrs={'href': re.compile('\/stargazers')})
    stars = int(stars.get_text(strip=True).replace(',', '') if stars else 0)
    print(name, language, stars)

# ------------------------------------------------------
"""
L6
"""
url = 'https://github.com/{}'
username = 'erfansafarzad7'

session = requests.Session()
req = session.get(url.format('login'))
content = BeautifulSoup(req.text, 'html.parser')

data = {}

for form in content.find_all('form'):
    for inp in form.select('input[type=hidden]'):
        data[inp.get('name')] = inp.get('value')

data.update({'login': '', 'password': ''})

req = session.post(url.format('session'), data=data)
req = session.get(url.format(username))
content = BeautifulSoup(req.text, 'html.parser')
user_info = content.find(class_='vcard-details')

# print(user_info.text)

# ------------------------------------------------------
"""
L9
"""
qualities = {
    '144': 0,
    '240': 1,
    '360': 2,
    '480': 3,
    '720': 4,
    '1080': 5,
}


class VideoDownloadException(Exception):
    pass


class QualityError(VideoDownloadException):
    pass


class Scraper:
    def __init__(self, url, quality):
        self.url = url
        self.quality = quality

    def get_all_links(self):
        result = requests.get(self.url)
        content = BeautifulSoup(result.text, 'html.parser')
        video_links = content.find_all('a', href=re.compile('.mp4'))
        links = [link['href'] for link in video_links]
        links.reverse()
        return links

    def get_link(self):
        links = self.get_all_links()
        available_qualities = self.get_qualities()
        if self.quality not in available_qualities:
            raise QualityError(f'This quality is not available \n available qualities are {available_qualities}')
        else:
            link = links[qualities[self.quality]]
            return link

    def get_qualities(self):
        links = self.get_all_links()
        qua = list(qualities.keys())
        available_qualities = []
        for i in range(len(links)):
            available_qualities.append(qua[i])
        return available_qualities


class Main:
    def __init__(self, url, quality):
        self.url = url
        self.quality = quality
        self.scraper = Scraper(url, quality)

    def download(self):
        video_url = str(self.scraper.get_link())
        with open('video.mp4', 'wb') as f:
            print('Downloading...')
            result = requests.get(video_url, stream=True)
            total = result.headers.get('content-length')

            if total is None:
                f.write(result.content)
            else:
                download = 0
                total = int(total)
                for data in result.iter_content(chunk_size=4096):
                    f.write(data)
                    download += len(data)
                    done = int(50 * download / total)
                    print('\r[{}{}]'.format('=' * done, ' ' * (50 - done)), end='')
        print('\n Video Downloaded')


# https://www.namasha.com/v/jXPFYDcU
# a = Main(url='', quality='144')
# a.download()

# ------------------------------------------------------

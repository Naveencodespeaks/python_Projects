import requests
from bs4 import Beautifulsoup

url = 'https://www.codewithtomi.ml/'
r = requests.get(url)
print(r)
soup = Beautifulsoup(r.content, 'lxml')
title =soup.find_all('h2', {'class' : 'post-title'})
print(title)
print(title.getText())
title1 = title[0].getText()
print(title1)

for t in title:
    print(t.getText())


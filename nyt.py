#!/usr/bin/ python
import requests
from bs4 import BeautifulSoup
import datetime
from collections import Counter
import os


sections = ['opinion','world','business']
#sections.append('technology')
#sections.append('us')
#sections.append('arts')
max_sec_val = 5 #maximum number of articles to open per section
save_dir = os.getenv('HOME') #directory where hidden file with urls to open

section_counts = Counter() 
urls_open = []
r = requests.get('http://www.nytimes.com/')
today = datetime.date.today()
dstr = today.strftime('%Y/%m/%d')
soup = BeautifulSoup(r.text, 'html.parser')
for art in soup.find_all('article'):
    for a in art.find_all('a' ,href=True):
        the_url = a.get('href')
        if the_url.startswith('http://www.nytimes.com/'+dstr):
#             print(the_url.split('http://www.nytimes.com/'))
            sec = the_url.split(dstr)[1].split('/')[1]
            if sec in section_counts.keys():
                section_counts.update({sec: 1})
                if section_counts[sec] < max_sec_val:
                    urls_open.append(the_url)
#             print(sec)
        break

# pprint(urls_open)
with open(save_dir+'/.nyt_articles.txt', 'w') as f:
    f.write('\n'.join(urls_open)+'\n')

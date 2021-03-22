from bs4 import BeautifulSoup
import requests, re

r = requests.get('http://scp-wiki.wikidot.com/scp-series').content
soup = BeautifulSoup(r, "lxml")

# tags = soup.find_all("li", {"class":re.compile('(scp)')})
# for scp in tags:
#     # print(p)
#     a = scp.findAll("li",{"scp":tags.text})
#     print(a[0].string)

# a_all = soup.find_all('a', attrs={'href':re.compile("/scp-+[0-9]")})
# li_all = soup.find_all('li', attrs={'li':re.compile('(scp)')})
# for li_all in li_all:
#     print('---')
#     print('name:', li_all.text)
# for a_all in a_all:
#     print('---')
#     print('all:',a_all)
#     print('info:',a_all.text)
    # print('li的属性:',li_all.attrs)
tags = soup.find_all("div", {"class":re.compile('(content-panel standalone series)')})
for li in tags:
    # print(p)
    a = li.findAll("li")
    print('---')
    print('the scp info:',li.text)
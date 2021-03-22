from bs4 import BeautifulSoup
import requests, re

r = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/computers').content
soup = BeautifulSoup(r, "lxml")
# tags = soup.find_all("a", {"href":re.compile('(allinone)')})
# for a in tags:
#     print(a.get('href'))

tags = soup.find_all("div", {"class":re.compile('(ratings)')})
# print(tags)
for p in tags:
    # print(p)
    a = p.findAll("p",{"class":"pull-right"})
    print(a[0].string)
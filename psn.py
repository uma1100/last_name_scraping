# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

url = "https://myoji-yurai.net/prefectureRanking.htm?prefecture=%E5%85%A8%E5%9B%BD&page=2"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

# タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
# title_tag = soup.find_all(class_="simple",id=None)

# # 要素の文字列を取得する → 経済、株価、ビジネス、政治のニュース:日経電子版
# title = title_tag.string
data = ''
for text in soup.find_all(class_="odd"):
	for psn in text.find_all("td"):
		if psn.a != None:
			data += '\r\n' + str(psn.a.string)

path_w = "/vg_workspace/text/psn1001~1500.txt"

with open(path_w, mode='w') as f:
    f.write(data)

with open(path_w) as f:
    print(f.read())


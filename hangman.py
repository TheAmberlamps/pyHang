import random

from requests_html import HTMLSession

session = HTMLSession()

url = 'https://www.randomlists.com/random-words?qty=1&dup=false'

r = session.get(url)

r.html.render()

session.close()

words = r.html.find(".base_title__Yd1Gv")

for entry in words:
  print(entry.text)

from pyquery import PyQuery as pq
import urllib
import re
import sys
import wget
import html2text
import os

if not os.path.exists("images"):
  os.mkdir("images")

def convert_and_save_page(page):
  baseurl = "https://docs.microsoft.com/en-gb/typography/opentype/spec/"
  output = page+".md"
  d = pq(url=baseurl + page, opener=lambda url: urllib.urlopen(url).read())
  html = d("#main").html()
  r = re.compile('<ul.*<content> -->', re.DOTALL)
  html = re.sub(r,'',html)

  md = html2text.html2text(html)

  for m in re.finditer('<img.*src="([^"]+)"',md):
    image = m.group(1)
    print("Fetching image "+image)
    wget.download(baseurl+image, image)

  print("Writing "+output)
  with open(output, 'w') as f:
      f.write(md.encode('utf8'))

with open('README.md', 'r') as file:
  index = file.read()
  for m in re.finditer("\(([^\)]+).md\)", index):
    convert_and_save_page(m.group(1))

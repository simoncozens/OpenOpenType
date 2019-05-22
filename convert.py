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

  for m in re.finditer('<img.*src="([^"]+)"',html):
    image = m.group(1)
    print("Fetching image "+image)
    wget.download(baseurl+image, image)

  md = html2text.html2text(html)

  # Fix up tables. If we are inside a table, we cannot have a non-table line
  def replacer(match):
    m1 = match.group(1)
    m2 = match.group(2)
    m3 = match.group(3)
    if re.match("\S", m2):
      m2 = re.sub("\n"," ",m2)
      return m1 + " " + m2 + "\n"
    else:
      return m1 + "\n" + m2 + "\n"

  md = re.sub('(.*\|.*)\n([^\|]+)\n(?=(.*\|.*))', replacer, md)

  # Fix up hex encoding
  md = re.sub(r'((?:\\x[0-9A-F]+)+)', r'`\1`', md)

  print("Writing "+output)
  with open(output, 'w') as f:
      f.write(md.encode('utf8'))

with open('README.md', 'r') as file:
  index = file.read()
  for m in re.finditer("\(([^\)]+).md\)", index):
    convert_and_save_page(m.group(1))

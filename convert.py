from pyquery import PyQuery as pq
import urllib
import re
import sys
import wget
import html2markdown

def convert_and_save_page(page):
  baseurl = "https://docs.microsoft.com/en-gb/typography/opentype/spec/"
  output = page+".md"
  d = pq(url=baseurl + page, opener=lambda url: urllib.urlopen(url).read())
  md = html2markdown.convert(d("#main").html())
  md = re.sub('<h1[^>]*>(.*)</h1>', r"# \1", md)
  md = re.sub('<h2[^>]*>(.*)</h2>', r"## \1", md)
  md = re.sub('<h3[^>]*>(.*)</h3>', r"### \1", md)
  md = re.sub('<a data-linktype="relative-path" href="([^#"]+)(#?[^"]*)">([^<]+)</a>',r'[\3](\1.md\2)',md)
  md = re.sub('<a data-linktype="self-bookmark" href="(#?[^"]*)">([^<]+)</a>',r'[\2](\1)',md)
  r = re.compile('<ul.*<content> -->', re.DOTALL)
  md = re.sub(r,'',md)
  md = re.sub('<!--.*-->','',md)
  r = re.compile('\n[\n\s]+', re.MULTILINE)
  md = re.sub(r,'\n\n',md)

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
    
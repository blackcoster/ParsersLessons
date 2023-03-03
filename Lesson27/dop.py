
from bs4 import BeautifulSoup
html = '<p class="title"><b>The Dormouses story</b></p>'
p = BeautifulSoup(html, 'html.parser')
# print(p)
print()
deti = p.children
for child in deti:
      print(child)
print()
for child in p.descendants:
      print(child)

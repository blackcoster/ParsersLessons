from bs4 import BeautifulSoup

with open('primer.html') as file:
    src = file.read()

soup = BeautifulSoup(src,'html.parser')
print(soup.h1.text)
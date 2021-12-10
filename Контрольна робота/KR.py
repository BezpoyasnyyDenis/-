import requests
from bs4 import BeautifulSoup
import sys

filename = open('kr.txt', 'w')
sys.stdout = filename

url = "https://www.pcgamer.com/the-witcher-books/"
serv = requests.get(url)
service = BeautifulSoup(serv.text, 'html.parser')

def get_text(url):
    rs = requests.get(url)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('article')
    return article.text

url = 'https://www.pcgamer.com/the-witcher-books/'
text = get_text(url)
txt = print(text[:50000]) 

for words in text.split(): 
    if(words.startswith("f")): 
        print(words)
        
filename.close()
sys.stdout = sys.__stdout__
with open('kr.txt') as file:
    data = file.read()
    print (data)


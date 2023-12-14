import requests
from bs4 import BeautifulSoup

URL = "https://www.wikihow.com/Make-a-Snowman"
page = requests.get(URL)

#print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("img") # class_="whcdn content-fill"

#print(results)


for res in results:
    print(res, end="\n"*2)
import requests
from bs4 import BeautifulSoup
from random import randint 
from time import sleep 

def method1(URL):
    req = requests.get(URL)
    soup = BeautifulSoup(req.content, "html.parser")
    results = soup.find_all("a")

    for res in results:
        res_descendants = res.descendants
        for d in res_descendants:
            if d.name == 'img' and d.get('src'):
                img0 = d['src']
                if img0[-3:-1] != 'png' or 'svg':
                    print('img: ', 'https://www.wikihow.com'+ img0)
                    img1 = 'https://www.wikihow.com'+ img0
                    
            elif d.name == 'p':
                cap1 = d.text
                print('alt: ', d.text)
            return cap1, img1
        
    #print(res.get('href')) # => add to URL list
                
def method2(URL):
    req = requests.get(URL)
    soup = BeautifulSoup(req.content, "html.parser")
    results1 = soup.find_all("img", alt=True, src=True)

    for res in results1:
        cap2 = res['alt']
        img2 = res['src']
        print(img2[-4:-1])
        if img2[-4:-1] != '.png' or '.svg':
            print(cap2, img2, end="\n"*2)
        return cap2, img2



URL = "https://www.wikihow.com/Main-Page/"

def scrape():
    




    #sleep(randint(2,10))


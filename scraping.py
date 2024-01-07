import requests
from bs4 import BeautifulSoup
from random import randint 
from time import sleep 

def method1(URL):
    req = requests.get(URL)
    soup = BeautifulSoup(req.content, "html.parser")
    results = soup.find_all("a")

    for res in results:
        l = res.get('href')
        print(l)
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
            return cap1, img1, l


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
    
def link2(URL):
    req = requests.get(URL)
    soup = BeautifulSoup(req.content, "html.parser")
    results2 = soup.find_all("a", href=True, rel=True)
    for r in results2:
        l = r['href']
        if l[0] == '/':
            print('https://www.wikihow.com'+l)
        return 'https://www.wikihow.com'+l



url = ["https://www.wikihow.com/Main-Page/"]
done = []

def scrape():
    while len(url) != 0:
        for u in url:
            if u not in done:
                done.append(u)
                # main page method:
                if u[-10:] != '/Main-Page/':
                    caption1, picture1, link1 = method1(u)
                    if link1 not in done:
                        url.append(link1)
                else:
                    caption2, picture2 = method2(u)
                    l = link2(u)
                    if l not in done:
                        url.append(l)


    #sleep(randint(2,10))
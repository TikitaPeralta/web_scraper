import requests
from bs4 import BeautifulSoup
from random import randint 
from time import sleep 
'''
def img1(URL):
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
                return img1, l

def cap1(URL):
    req = requests.get(URL)
    soup = BeautifulSoup(req.content, "html.parser")
    results = soup.find_all("a")
    for res in results:
        res_descendants = res.descendants
        for d in res_descendants:      
            if d.name == 'p':
                caption = d.text
                print('alt: ', d.text)
                return caption
'''            
def find_img_text_pairs(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    results = soup.find_all("a")
    new_results = []
    for res in results:
        tags_in_descendents = []
        if res.descendants is not None:
            for d in res.descendants:
                if d.name is not None:
                    tags_in_descendents.append(d.name)
        if "img" in tags_in_descendents and "p" in tags_in_descendents:
            new_results.append(res)
    two_results = []
    for res in new_results:
        for d in res.descendants:
            if d.name == "img" and d.get('src'):
                source = d['src']
                if source[-4:] != '.png' and source[-4:] != '.svg': 
                    two_results.append(res)
                break
    fin = []
    for r in two_results:
        #print(r)
        link0 = r.get('href')
        link1 = 'https://www.wikihow.com'+ link0
        #print(link1) # imgs
        for t in r.descendants:
            s = soup.find("div", class_="content-spacer")
            for i in s.descendants:
                #print(i)
                if i.name == 'img' and i.get('src'):
                    print(i['src'])
            if t.name == 'p':
                fin.append([link1, t.text])
                #print(t.text)
            

    #print(f"{len(results)} vs {len(new_results)} vs {len(two_results)}")

    print(fin)
    return fin


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



url = ["https://www.wikihow.com/Main-Page/", "https://www.wikihow.com/Improve-Your-Personality"]
done = []

def scrape():
    while len(url) != 0:
        for u in url:
            if u not in done:
                done.append(u)
                # main page method:
                if u[-10:] != 'Main-Page/':
                    picture1, link1 = img1(u)
                    caption1 = cap1(u)
                    #if link1 not in done:
                    #    url.append(link1)
                    print('caption1: ', caption1, 'picture1: ', picture1)
                else:
                    caption2, picture2 = method2(u)
                    #l = link2(u)
                    #if l not in done:
                    #    url.append(l)
                    print('caption2: ', caption2, 'picture2: ', picture2)

#scrape()
    #sleep(randint(2,10))

URL = "https://www.wikihow.com/Main-Page/"
pairs = find_img_text_pairs(URL)
print(pairs)
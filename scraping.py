import requests
from bs4 import BeautifulSoup
from random import randint 
from time import sleep 

#URL = "https://www.wikihow.com/Main-Page/"

url = ["https://www.wikihow.com/Main-Page/", "https://www.wikihow.com/Improve-Your-Personality"]
done = []
'''
while len(url) != 0:
    for u in url:
        if u not in done:
            #method1: main page
            if u[-10:] == 'Main-Page/':
                req = requests.get(u)
                soup = BeautifulSoup(req.content, "html.parser")

                results = soup.find_all("a")
                done.append(u)
                for res in results:
                    res_descendants = res.descendants
                    for d in res_descendants:
                        if d.name == 'img' and d.get('src'):
                            print('img: ', 'https://www.wikihow.com'+d['src'])
                        if d.name == 'p':
                            print('alt: ', d.text)

                    link = res.get('href')
                    print(link) # => add to URL list
                    #u.append(link)
                
            else:
                # method2: branch page
                req = requests.get(u)
                soup = BeautifulSoup(req.content, "html.parser")
                results1 = soup.find_all("img", alt=True, src=True)
                results2 = soup.find_all("a", href=True)
                for r in results2:
                    print(res['href'])

                for res in results1:
                    print(res['alt'], res['src'], end="\n"*2)
            
            print('url: ', url, 'done: ', done)

'''
#sleep(randint(2,10))

req = requests.get("https://www.wikihow.com/Improve-Your-Personality")
soup = BeautifulSoup(req.content, "html.parser")
results2 = soup.find_all("a", href=True, rel=True)
for r in results2:
    if '#' not in r:
        print(r['href'])
    #print('https://www.wikihow.com'+r['href'])
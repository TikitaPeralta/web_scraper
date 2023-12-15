import requests
from bs4 import BeautifulSoup
from random import randint 
from time import sleep 

URL = "https://www.wikihow.com/Main-Page/"

#for page in range(1, 3):
req = requests.get(URL)
#print(req.text)
soup = BeautifulSoup(req.content, "html.parser")

#method1: main page
results = soup.find_all("a")

for res in results:
    #print(res, end="\n"*2)
    res_descendants = res.descendants
    for d in res_descendants:
        #print('d: ', d, end='\n'*2)
        if d.name == 'img' and d.get('src'):
            print('img: ', 'https://www.wikihow.com'+d['src'])
        if d.name == 'p':
            print('alt: ', d.text)
        
    #print(res.get('href')) # => add to URL list

'''
# method2: branch page
results1 = soup.find_all("img", alt=True, src=True)

for res in results1:
    print(res['alt'], res['src'], end="\n"*2)
'''
    
#sleep(randint(2,10))


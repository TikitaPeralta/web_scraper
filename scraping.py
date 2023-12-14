import requests
from bs4 import BeautifulSoup
from random import randint 
from time import sleep 
import sys
import cv2

URL = "https://www.wikihow.com/Make-a-Snowman"

'''
req = requests.get(URL)
soup = BeautifulSoup(req.content, "html.parser")

results2 = soup.find_all("a")

for res in results2:
    print(res, end="\n"*2)
#children = results2.findChildren()
#para = results2.contents[1]

#for pa in para:
    #print(pa, end="\n"*2)
'''

#for page in range(1, 3):
req = requests.get(URL)
#print(req.text)
soup = BeautifulSoup(req.content, "html.parser")

results = soup.find_all("img", alt=True, src=True)

for res in results:
    print(res['alt'], res['src'], end="\n"*2)
    #img = cv2.imread(res['src'], cv2.IMREAD_ANYCOLOR)
    #cv2.imshow(res['alt'], img)
    #cv2.waitkey(0)
    #sys.exit()

#cv2.destroyAllWindows()
    

#nmmyhgvfvvsleep(randint(2,10))


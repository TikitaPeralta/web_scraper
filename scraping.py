import requests
import urllib.request
from pathlib import Path
import pathlib
import os
from bs4 import BeautifulSoup
from random import randint 
from time import sleep
import json
from PIL import Image

# main page method:
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
        link0 = r.get('href')
        link1 = 'https://www.wikihow.com'+ link0
        for t in r.descendants:
            if t.name == 'img' and t.get('src'):
                img1 = 'https://www.wikihow.com'+t['src']
                #print(img1)
            if t.name == 'p':
                fin.append([link1, t.text, img1])
            
    return fin

# any other page method:
def method2(URL):
    req = requests.get(URL)
    soup = BeautifulSoup(req.content, "html.parser")
    results1 = soup.find_all("img", alt=True, src=True)
    final = []
    for res in results1:
        cap2 = res['alt']
        img2 = res['src']
        if img2[-4:] != '.png' and img2[-4:] != '.svg':
            final.append([cap2, img2])
    return final
    
def link(URL):
    req = requests.get(URL)
    soup = BeautifulSoup(req.content, "html.parser")
    results2 = soup.find_all("a", href=True, rel=True)
    links = []
    for r in results2:
        l = r['href']
        if l[0] == '/':
            links.append('https://www.wikihow.com'+l)
    return links



url = ["https://www.wikihow.com/Main-Page/", "https://www.wikihow.com/Improve-Your-Personality"]
done = []

def scrape(url, done):
    while len(url) != 0:
        for u in url:
            if u not in done:
                done.append(u)
                url.remove(u)
                print('url: ', url, ' | done: ', done)
                sleep(randint(2,10))
                # main page method:
                if u[-10:] == 'Main-Page/':
                    res = find_img_text_pairs(u)
                    cap_img = []
                    for r in res:
                        link1 = r[0]
                        caption1 = r[1]
                        picture1 = r[2]
                    if link1 not in done:
                        url.append(link1)
                        cap_img.append([caption1, picture1])
                    data = []
                    for index, item in enumerate(cap_img):
                        d = {
                            f'id {index}' : [
                                {
                            'caption' : f"{item[0]}",
                            'imgLink' : f'{item[1]}',
                            'path' : f'/home/tikitaperalta/web_scraper/wikihowImgs/{item[1]}'
                                }
                            ]
                        }
                        data.append(d)
                        with open("./jsonFile.txt", "w") as file:
                            json_data = json.dump(data, file)
                            print(json_data)
                        try:
                            response = requests.get(item[1])
                            file_name = item[1].split('/')[-1]
                            file_path = os.path.join('wikihowImgs', file_name)
                            if response.status_code == 200:
                                with open(file_path, 'wb') as f:
                                    f.write(response.content)
                            else:
                                print(f"Failed to download the image. Status code: {response.status_code}")
                        except Exception as e:
                            print(f"An error occurred: {e}")
                else:
                    res1 = method2(u)
                    l = link(u)
                    if l not in done:
                        url.append(l)
                    r = []
                    for i in res1:
                        caption2 = i[0]
                        if i[1][:23] == 'https://www.wikihow.com':
                            picture2 = i[1]
                        else:
                            picture2 = 'https://www.wikihow.com' + i[1]
                        r.append([caption2, picture2])
                    data2 = []
                    for ind, ite in enumerate(r):
                        d2 = {
                            f'id {ind}' : [
                                {
                            'caption' : f"{ite[0]}",
                            'imgLink' : f'{ite[1]}',
                            'path' : f'/home/tikitaperalta/web_scraper/wikihowImgs/{ite[1]}'
                                }
                            ]
                        }
                        data2.append(d2)
                        with open("./jsonFile.txt", "w") as file:
                            json_data2 = json.dump(data2, file)
                            print(json_data2)
                        try:
                            response = requests.get(ite[1])
                            file_name = ite[1].split('/')[-1]
                            file_path = os.path.join('wikihowImgs', file_name)
                            if response.status_code == 200:
                                with open(file_path, 'wb') as f:
                                    f.write(response.content)
                            else:
                                print(f"Failed to download the image. Status code: {response.status_code}")
                        except Exception as e:
                            print(f"An error occurred: {e}")

scrape(url, done)

#path = os.getcwd()
#print(path)
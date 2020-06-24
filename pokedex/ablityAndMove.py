import requests
from bs4 import BeautifulSoup
import pymongo
import json

#函数
def changekey(dicts):
    for key in dicts:
        if(isinstance(dicts[key],list)):
            for i in dicts[key]:
                if(isinstance(i,dict)):
                    changekey(i)
        if(isinstance(dicts[key],dict)):
            changekey(dicts[key])
        if (key.find('.')>0):
            print(dicts[key])
            new = key.replace(".", "-")
            print(new)
            dicts[new] = dicts.pop(key)

if __name__=="__main__":
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    myclient = pymongo.MongoClient("mongodb://116.62.200.15:27017")
    mydb = myclient["pokedex"]
    mycol = mydb["pokemon"]
    # url
    url = "https://www.pokedex.app/zh/pokemon-139"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, features="html.parser")
    script = soup.find_all('script')
    data = script[-2].text[52:-75].strip()
    data = data[:-5]
    print(data)
    dicts = json.loads(data)
    del dicts["moves"]
    if "forme" in dicts:
        forme = dicts["forme"]
        for i in forme:
            if "moves" in i:
                del i["moves"]
    print(dicts)
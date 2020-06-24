import requests
from bs4 import BeautifulSoup
import pymongo
import json

#函数
def changekey(dicts):
    for key in dicts:
        if (key.find('.')>0):
            new = key.replace(".", "-")
            dicts[new] = dicts.pop(key)
            key=new
            print(key,dicts[key])
        if(isinstance(dicts[key],list)):
            for i in dicts[key]:
                if(isinstance(i,dict)):
                    changekey(i)
        if(isinstance(dicts[key],dict)):
            changekey(dicts[key])


if __name__=="__main__":
    # 主体
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    myclient = pymongo.MongoClient("mongodb://116.62.200.15:27017")
    mydb = myclient["pokedex"]
    mycol = mydb["pokemon"]
    # url
    for i in range(139, 891):
        url = "https://www.pokedex.app/zh/pokemon-" + str(i)
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, features="html.parser")
        script = soup.find_all('script')
        data = script[-2].text[52:-75].strip()
        data = data[:-5]
        dicts = json.loads(data)
        del dicts["moves"]
        if "forme" in dicts:
            forme = dicts["forme"]
            for i in forme:
                if "moves" in i:
                    del i["moves"]
        try:
            success = mycol.insert_one(dicts)
            print("插入成功"+str(i))
        except:
            print("插入失败"+str(i))


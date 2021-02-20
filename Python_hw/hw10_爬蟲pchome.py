import requests
import codecs
import json
import prettytable as pt
import os

kwd=input("關鍵字：")
r1=requests.get(
    "https://ecshweb.pchome.com.tw/search/v3.3/all/results",
    params={
        "q":"%s"%(kwd),
        "page":"1"
        ,"sort":"sale/dc"
    }
)
os.system("cls")
r1.encoding="utf-8"
ret=r1.json()
t=pt.PrettyTable()
t.field_names=["名稱","價格"]
t.align="l"
for d in ret["prods"]:
    t.add_row([d["name"],d["price"]])
print(t)


while True:
    pge=input("頁碼：")
    r2=requests.get(
        "https://ecshweb.pchome.com.tw/search/v3.3/all/results",
        params={
            "q":"%s"%(kwd),
            "page":"%s"%(pge),
            "sort":"sale/dc"
        }
    )

    os.system("cls")
    r2.encoding="utf-8"
    try:
        ret=r2.json()
    except:
        print("頁碼超過範圍!")
        os.system("pause")
        break
    t=pt.PrettyTable()
    t.field_names=["名稱","價格"]
    t.align="l"
    for d in ret["prods"]:
        t.add_row([d["name"],d["price"]])
    print(t)
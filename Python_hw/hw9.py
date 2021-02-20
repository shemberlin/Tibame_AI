import requests
import codecs

r1=requests.get(
    "http://teaching.bo-yuan.net/test/requests/" ,
    params={
         "action":"jjj"
    }
)
r2=requests.delete("http://teaching.bo-yuan.net/test/requests/" ,
    params={
         "action":"jjj"
    },
     data={"id":"xxxx"
    } 
)
r3=requests.put("http://teaching.bo-yuan.net/test/requests/" ,
    params={"action":"jjj"},
    data={"id":"xxxx","name":"xxxx"}
)
r4=requests.patch("http://teaching.bo-yuan.net/test/requests/" ,
    params={"action":"jjj"},
    data={"id":"xxxx","name":"xxxx","address":"hhb"}   
)
r5=requests.post("http://teaching.bo-yuan.net/test/requests/" ,
    params={"action":"jjj"},
    data={"id":"xxxx","name":"xxxx","address":"hhb"}   
)


# print(r1.status_code)
# print(r1.headers)
# print(r1.encoding)
r1.encoding="utf8"
print(r1.text)
r2.encoding="utf8"
print(r2.text)
r3.encoding="utf8"
print(r3.text)
r4.encoding="utf8"
print(r4.text)
r5.encoding="utf8"
print(r5.text)
# with codecs.open("html/1.html","w",r1.encoding) as f:
#      f.write(r1.text)
# with codecs.open("html/1.jpg","wb",r1.encoding) as f:
#      f.write(r1.content)
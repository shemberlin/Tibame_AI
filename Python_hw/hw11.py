import requests
import prettytable as pt
from bs4 import BeautifulSoup

r1=requests.get(
	"https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html"
)

b1=BeautifulSoup(r1.text,"html.parser")
a1=b1.find_all("tr")

table=pt.PrettyTable(["地區","氣溫"])
table.align="l"
for d1 in a1:
    table.add_row([d1.find("th").text,d1.find("span").text+" ℃"])

print(table)

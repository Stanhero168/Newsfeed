import sys
import subprocess
import requests
import html5lib
from bs4 import BeautifulSoup

ticker = sys.argv[1]

url = "https://finance.yahoo.com/quote/" + ticker + "/?p=" + ticker

req = requests.get(url)

soup = BeautifulSoup(req.text,'html5lib')

result = soup.find_all('li',{'class':'js-stream-content'})

print("\n")

for every in result[:5:]:

	time = every.find('div', {'class':'C(#959595) Fz(11px) D(ib) Mb(6px)'})

	time2 = time.find_all('span')[1].text

	time3 = "<< " + time2 + " >>"

	two = every.find('a')

	three = two.get("href")

	theLink = "https://finance.yahoo.com/" + three

	theInfo = time3 + "\n\n" + two.text + "\n" + theLink + "\n"

	four = "start " + theLink

	subprocess.call(four,shell=True)

	print(theInfo)


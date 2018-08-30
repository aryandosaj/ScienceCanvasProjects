from bs4 import *
import webbrowser
import requests
import re
import matplotlib.pyplot as plt
import numpy as np
abc=["USD","EUR","GBP","INR","AUD"]
ccc={
    "USD" : [],
    "EUR" : [],
    "GBP" : [],
    "INR" : [],
    "AUD" : []

}
url='http://www.xe.com/currencyconverter/'
chart=requests.get(url)
chart1=BeautifulSoup(chart.text,"html.parser")
chart2=chart1.find('div',{'id':'xRatesBx'})
print("CURRENT CURRENCY CONVERSION RATES")


x=0;
for i in chart2.find_all('a'):
    a=i.get('rel')
    z=x%4

    if a:
        print("1",(a[0].split(','))[1]," = ",i.string,(a[0].split(','))[0])
        ccc[(a[0].split(','))[1]].insert(z,(float(i.string)))
        x=x+1


pos= np.arange(4)+2
fig=plt.figure()
rect=fig.patch
rect.set_facecolor('grey')
graph1=fig.add_subplot(3,2,1,axisbg="black")
graph1.barh(pos,ccc["USD"],align="center",color='blue')
graph1.set_title("1 USD =",color='white')
graph1.set_yticklabels(('','EUR','','GBP','','INR','','AUD'),color='white')
graph2=fig.add_subplot(3,2,2,axisbg="black")
graph2.barh(pos,ccc["EUR"],align="center",color='white')
graph2.set_title("1 EUR =",color='white')
graph2.set_yticklabels(('','USD','','GBP','','INR','','AUD'),color='white')
graph3=fig.add_subplot(3,2,3,axisbg="black")
graph3.barh(pos,ccc["GBP"],align="center",color='orange')
graph3.set_title("1 GBP =",color='white')
graph3.set_yticklabels(('','USD','','EUR','','INR','','AUD'),color='white')
graph4=fig.add_subplot(3,2,4,axisbg="black")
graph4.set_title("1 INR =",color='white')
graph4.barh(pos,ccc["INR"],align="center",color='green')
graph4.set_yticklabels(('','USD','','EUR','','GBP','','AUD'),color='white')
graph5=fig.add_subplot(3,2,5,axisbg="black")
graph5.barh(pos,ccc["AUD"],align="center",color='gold')
graph5.set_title("1 AUD =",color='white')
graph5.set_yticklabels(('','USD','','EUR','','GBP','','INR'),color='white')

plt.show();



add='https://www.google.co.in/search?source=hp&ei=WA7_WY2CDoHtvgSc3o6IDQ&q=25+****+in+####&oq=25+****+in+####&gs_l=psy-ab.12..35i39k1j0i22i30k1l2.13920.39593.0.147504.41.35.3.0.0.0.451.6118.2-11j4j4.20.0....0...1.1.64.psy-ab..18.22.6003.6..0j0i13k1j0i13i5i10i30k1j0i13i10k1j0i10k1j0i131k1j0i67k1j0i20i263k1j0i10i67k1.247.uWnL5lyKaJU'
curr1=input('Enter the currency you want to convert from')
curr2=input('Enter the currency you want to convert to')
num=input('Enter the amount')
add=add.replace('****',curr1)
add=add.replace('####',curr2)
add=add.replace('25',num)
page=requests.get(add)

soup=BeautifulSoup(page.text,"html.parser")
data=soup.find('table',{'class':'std _tLi'})
data2=data.find('b')
print(data2.string)


from numpy import *
from matplotlib import  *
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('forestfires.csv')

x = data.iloc[:,[0,1,4,5,6,7,8,9,10,11]].values
y = data.iloc[:,[12]].values
constants =[1,3.0,2.0,100.0,1.0,1,1,1,1,1]
alpha = [0.000001,0.000001,0.000001,0.000001,0.0000001,0.000001,0.000001,0.000001,0.000001,0.000001]
n=float(len(y))
def update():
    sigma = [0]*10
    global constants

    for (i,j) in zip(x,y):
        sigma+=((sum(i*constants)-j)*i)
    constants-=2/n*sigma*alpha 
for i in range(4000):
    update()


for (i,j) in zip(x,y):
    ans = sum(constants*i)
    if(ans<0):
        ans = 0
    print(ans,j)
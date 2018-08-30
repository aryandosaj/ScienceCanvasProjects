import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8]
y = [53807,55217,55209,55415,63100,63206,63761,65766]

c = 50000
m = 100
n = float(len(x))
alpha1 = 0.0001
alpha2 = 0.0001
def update():
    der_c = 0
    der_m = 0
    global c,m,alpha,n
    for (i,j) in zip(x,y):
        der_m =der_m + i*(m*i + c - j)
        der_c =der_c +  m*i + c - j

    m = m - alpha1 * 2 / n * der_m
    c = c - alpha2 * 2 / n * der_c

for i in range(2000):
    update()
print("Mean of x =",(sum(x)/n))
print("Mean of y =",(sum(y)/n))
print("Equaton of line : y = ",m,"x + ",c)
print("Prediction of Year 2010 = ",(m*(2010-1994) + c))
print("Prediction of Year 2017 = ",(m*(2017-1994) + c))
plt.plot(x,y,'o')
plt.plot([0,10],[c,10*m+c])
plt.show()







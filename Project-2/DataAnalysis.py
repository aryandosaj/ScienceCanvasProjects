import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('zoo.csv')
arr = data.iloc[:,:].values
print("Total Animals With Hair = ",data.sum().hair)
print("Total Animals with feathers = ",data.sum().feather)
print("Total Animals which lay Egg = ",data.sum().eggs)
print("Total Animals which praduce milk = ",data.sum().milk)
print("Total Airborne Animals = ",data.sum().airborne)
print("Total Aquatic Animals = ",data.sum().aquatic)
print("Total Predator Animals = ",data.sum().predator)
print("Total Toothed Animals = ",data.sum().toothed)
print("Total Animals with backbone = ",data.sum().backbone)
print("Total beather Animals = ",data.sum().beather)
print("Total venomous Animals = ",data.sum().venomous)
print("Total Animals with fins = ",data.sum().fins)
print("Total Domestic Animals = ",data.sum().domestic)
print('\n')
print('\n')
lis = [0]*17
print("Animals With Hair")
for i in range(101):
    if (arr[i][1]==1):
        print(arr[i][0])
        lis[0]=lis[0]+1
print('\n')
print("Animals With Feathers")
for i in range(101):
    if (arr[i][2]==1):
        print(arr[i][0])
        lis[1] = lis[1] + 1
print('\n')
print("Animals Which lay egg")
for i in range(101):
    if (arr[i][3]==1):
        print(arr[i][0])
        lis[2] = lis[2] + 1
print('\n')
print("Animals Which produce milk")
for i in range(101):
    if (arr[i][4]==1):
        print(arr[i][0])
        lis[3] = lis[3] + 1
print('\n')
print("Airborne Animals")
for i in range(101):
    if (arr[i][5]==1):
        print(arr[i][0])
        lis[4] = lis[4] + 1
print('\n')
print("Aquatic Animals")
for i in range(101):
    if (arr[i][6]==1):
        print(arr[i][0])
        lis[5] = lis[5] + 1
print('\n')
print("Predators")
for i in range(101):
    if (arr[i][7]==1):
        print(arr[i][0])
        lis[6] = lis[6] + 1
print('\n')
print("Animals With Teeth")
for i in range(101):
    if (arr[i][8]==1):
        print(arr[i][0])
        lis[7] = lis[7] + 1
print('\n')
print("Animals With Backbone")
for i in range(101):
    if (arr[i][9]==1):
        print(arr[i][0])
        lis[8] = lis[8] + 1

print('\n')
print("Venomous Animals")
for i in range(101):
    if (arr[i][11]==1):
        print(arr[i][0])
        lis[9] = lis[9] + 1
print('\n')
print("Animals With Fins")
for i in range(101):
    if (arr[i][12]==1):
        print(arr[i][0])
        lis[10] = lis[10] + 1

print('\n')
print("Animals With 2 legs")
for i in range(101):
    if (arr[i][13]==2):
        print(arr[i][0])
        lis[11] = lis[11] + 1
print('\n')
print("Animals With 4 legs")
for i in range(101):
    if (arr[i][13]==4):
        print(arr[i][0])
        lis[12] = lis[12] + 1
print('\n')
print("Animals With 6 legs")
for i in range(101):
    if (arr[i][13]==6):
        print(arr[i][0])
        lis[13] = lis[13] + 1
print('\n')
print("Animals With 8 legs")
for i in range(101):
    if (arr[i][13]==8):
        print(arr[i][0])
        lis[14] = lis[14] + 1


print('\n')
print("Animals With a tail")
for i in range(101):
    if (arr[i][14]==1):
        print(arr[i][0])
        lis[15] = lis[15] + 1

print("\n")
print("Domestic Animals")
for i in range(101):
    if (arr[i][14]==1):
        print(arr[i][0])
        lis[16] = lis[16] + 1
names = ["Hair","feather","eggs","milk","airborne","aquatic","predators","toothed","backbone","venomous","fins","2 legs","4 legs","6 leg","8 legs","tail","domestic"]
plt.barh(names,lis)
plt.xlabel("Number of animals")
plt.ylabel("Animal Categories")

plt.show()




























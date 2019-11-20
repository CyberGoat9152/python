"""
    powered by: Cybergoat

"""
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

arq = open("data/exampleData.csv", "r")#the name of csv files goes here

for line in arq.readlines():
    data = line.replace("\n", "").replace(",", ".").split(";") #csv separed with ; (change for your use)
    x.append( float( data[0] ) )
    y.append( float( data[1] ) ) #make sure y is your 2 column on csv, or change the column
limiteSuperior = 0

fig, ax = plt.subplots()
"""
ax.plot(list(range(len(y))), y, 'b--', label='Curve label')
ax.plot(list(range(len(y))), y, 'go', markersize=2 )
"""
ax.plot(x, y, 'b-', label='Curve label')


plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.title("title of your graph")

ax.grid()
ax.legend()

plt.savefig("yourGraph.png")#name of file
plt.show()
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("new.csv")
mass = df["Mass"].tolist()
radius = df["Radius"].tolist()

X = np.reshape(mass, (len(mass), 1))
Y = np.reshape(radius, (len(radius), 1))

#Code for line plot
#plt.plot(X, Y, color='red', linewidth=3)

sizes = np.random.uniform(15, 80, len(X))
colors = np.random.uniform(15, 80, len(X))

fig, ax = plt.subplots()
ax.scatter(X, Y, s=sizes, c=colors, vmin=0, vmax=100)

plt.ylabel('Y')
plt.xlabel('X')
plt.show()



   

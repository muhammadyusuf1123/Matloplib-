# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XzzhQ6MEmlhR2v6p4UM3vtf-eBIG7KCD
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,6])
y=np.array([0,250])

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,6,8])
y=np.array([3,8,1,10])

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, 1000)

heart_rate = np.sin(2 * np.pi * 1 * t) + 0.5 * np.sin(2 * np.pi * 2 * t)

plt.plot(t, heart_rate, label="Yurak urishi")
plt.title("Yurak urishi ritmi")
plt.xlabel("Vaqt (sekund)")
plt.ylabel("Amplituda")
plt.grid(True)
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np


y=np.array([3,8,1,10])

plt.plot(y,'o:r')
plt.show()

import matplotlib.pyplot as plt
import numpy as np


y=np.array([3,8,1,10])

plt.plot(y, marker='o',ms=20)
plt.show()

import matplotlib.pyplot as plt
import numpy as np


y=np.array([3,8,1,10])

plt.plot(y, marker='o',ms=20,mec='r')
plt.show()

import matplotlib.pyplot as plt
house_x = [0, 0, 5, 5, 0]
house_y = [0, 5, 5, 0, 0]

roof_x = [-1, 2.5, 6, -1]
roof_y = [5, 8, 5, 5]

plt.plot(house_x, house_y, 'b-', label='Uyning asosiy shakli')
plt.plot(roof_x, roof_y, 'r-', label='Tom')

plt.fill(house_x, house_y, 'lightblue')
plt.fill(roof_x, roof_y, 'brown')

plt.xlim(-2, 7)
plt.ylim(0, 10)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Uy Shakli")

plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x1=np.array([0,1,2,3])
y1=np.array([3,8,1,10])
x2=np.array([0,1,2,3])
y2=np.array([6,2,7,11])

plt.plot(x1,y1,x2,y2)
plt.show()

import matplotlib.pyplot as plt
import numpy as np


y=np.array([3,8,1,10])

plt.plot(y, marker='o',ms=20,mfc='r')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,1,2,3,4,5])
y=np.array([0,8,12,20,26,38])

plt.scatter(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,0,5,5,5,0,2,2,1,1,3,3,4,4,0,0,0,0,5,5,5,5])
y=np.array([5,35,35,5,20,20,35,5,35,5,35,5,35,5,10,15,25,30,10,15,25,30])

plt.scatter(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,1,2,3,4,5])
y=np.array([0,2,8,1,14,7])

mycolor=['red','green','purple','lime','aqua','yellow']

plt.scatter(x,y,color=mycolor)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,1,2,3,4,5])
y=np.array([0,2,8,1,14,7])

mycolor=['red','green','purple','lime','aqua','yellow']
size=[10,60,120,80,20,190]

plt.scatter(x,y,color=mycolor,s=size)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,1,2,3,4,5])
y=np.array([0,2,8,1,14,7])

mycolor=['red','green','purple','lime','aqua','yellow']
size=[10,60,120,80,20,190]

plt.scatter(x,y,color=mycolor,s=size,alpha=0.3)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('photo_2020-09-25_11-26-00-xl_WB3AMpe')

x = 0.5 + np.array(8)
y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0 ,8), xticks=np,arange(1, 8),ylim=(0, 8), yticks=np.arange(1, 8))
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array(['A','B','C','D'])
y=np.array([3,8,1,10])

plt.bar(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array(['A','B','C','D'])
y=np.array([3,8,1,10])

plt.barh(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array(['A','B','C','D'])
y=np.array([3,8,1,10])

plt.bar(x,y,width=0.1)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([35,25,25,15])


plt.pie(y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([35,25,25,15])
mylabels = ["Apples","Bananas","Cherries","Dates"]

plt.pie(y,labels=mylabels)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([35,25,25,15])
mylabels = ["Apples","Bananas","Cherries","Dates"]

plt.pie(y,labels=mylabels,startangle=90)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([35,25,25,15])
mylabels = ["Apples","Bananas","Cherries","Dates"]
myexplode = [0.2,0,0,0]
plt.pie(y,labels=mylabels,startangle=90,explode=myexplode)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([35,25,25,15])
mylabels = ["Apples","Bananas","Cherries","Dates"]
myexplode = [0.2,0,0,0]
plt.pie(y,labels=mylabels,startangle=90,explode=myexplode,shadow=True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([35,25,25,15])
mylabels = ["Apples","Bananas","Cherries","Dates"]
mycolors = ["black","hotpink","b","#4CAF50"]
myexplode = [0.2,0,0,0]
plt.pie(y,labels=mylabels,startangle=90,explode=myexplode,colors=mycolors)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([35,25,25,15])
mylabels = ["Apples","Bananas","Cherries","Dates"]

plt.pie(y,labels=mylabels)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([35,25,25,15])
mylabels = ["Apples","Bananas","Cherries","Dates"]

plt.pie(y,labels=mylabels)
plt.legend(title='Four Fruits')
plt.show()
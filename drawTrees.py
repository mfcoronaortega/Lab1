#Course: CS 2302 Data Structures | Spring 2019
#Author: Maria Fernanda Corona Ortega
#Assignment: Lab 1 | Part 2 Figure 3
#Instructor: Olac Fuentes
#Purpose of Code: The purpose of this code is to duplicate images presented
#through plotting and recursion
#Last Modification: 03/09/2019 8:27pm
import numpy as np
import matplotlib.pyplot as plt

def figure3(ax,n,p,w):
    if n>0:
        index = [0,1,2]
        q = p[index]/2+p[index]
        ax.plot(p[:,0],p[:,1],color='k')
        figure3(ax,n-1,q,w)
        

plt.close("all") 
size = 3 
levels = 1
p = np.array([[-size,-size-(size/size)],[0,0],[size,-size-(size/size)]])
  
fig, ax = plt.subplots()

figure3(ax,levels,p,1/3) 

ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('figure3.png')
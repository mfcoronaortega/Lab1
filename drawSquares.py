#Course: CS 2302 Data Structures | Spring 2019
#Author: Maria Fernanda Corona Ortega
#Assignment: Lab 1 | Part 3 Figures 1
#Instructor: Olac Fuentes
#Purpose of Code: The purpose of this code is to duplicate images presented
#through plotting and recursion
#Last Modification: 03/09/2019 8:27pm
import numpy as np
import matplotlib.pyplot as plt

def figure1(ax,n,p,p1,p2,p3,p4,w): #FIXME
    if n>0:
        index = [1,2,3,0,1]
        q = p[index]
        q1 = p1[index]*w + 2*w
        q2 = w*p2[index]+ 2*w
        q3 = w*p3[index]+ 2*w
        q4 = w*p4[index]+ 2*w
        ax.plot(p[:,0],p[:,1],color='k')
        ax.plot(p1[:,0],p1[:,1],color='k')
        ax.plot(p2[:,0],p2[:,1],color='k')
        ax.plot(p3[:,0],p3[:,1],color='k')
        ax.plot(p4[:,0],p4[:,1],color='k')
        figure1(ax,n-1,q,q1+4*w,q2+4*w,q3+4*w,q4+4*w,w)
        figure1(ax,n-1,q,q1-4*w,q2-4*w,q3-4*w,q4-4*w,w) 
#        figure1(ax,n-1,q,q1,q2,q3,q4,w) 
#        figure1(ax,n-1,q,q1,q2*w,q3*w,q4*w,w)

plt.close("all") 
size = 4

p = np.array([[0,0],[0,size],[size,size],[size,0],[0,0]])
p1 = np.array([[-size/4,-size/4],[-size/4,size/4],[size/4,size/4],[size/4,-size/4],[-size/4,-size/4]])
p2 = np.array([[size-size/4,-size/4],[size-size/4,size/4],[size+size/4,size/4],[size+size/4,-size/4],[size-size/4,-size/4]])
p3 = np.array([[-size/4,size-size/4],[-size/4,size+size/4],[size/4,size+size/4],[size/4,size-size/4],[-size/4,size-size/4]])
p4 = np.array([[size-size/4,size-size/4],[size-size/4,size+size/4],[size+size/4,size+size/4],[size+size/4,size-size/4],[size-size/4,size-size/4]])


fig, ax = plt.subplots()
figure1(ax,4,p,p1,p2,p3,p4,.5)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('fig1.png')
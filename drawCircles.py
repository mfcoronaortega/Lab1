import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y
        
def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        draw_circles(ax,n-1,center,radius*w,w)
        
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 100, [100,0], 100,.9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')

def figure2(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x+radius,y,color='k')
        figure2(ax,n-1,center,radius*w,w)
        
plt.close("all") 
fig, ax = plt.subplots() 
figure2(ax, 100, [0,0], 100,.9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('figure2.png')


def figure4(ax,n,center,radius,w):

    if n>0:
        x,y = circle(center,radius)
        ax.plot(x*w,y*w,color='k')
        ax.plot(x*w+radius-radius*w,y*w,color='k')
        ax.plot(x*w-radius+radius*w,y*w,color='k')
        ax.plot(x*w,y*w-radius+radius*w,color='k')
        ax.plot(x*w,y*w+radius-radius*w,color='k')
        figure4(ax,n-1,center,radius*w,w)
        figure4(ax,n-1,[radius+radius,0],radius*w,w)
        figure4(ax,n-1,[radius-radius/w,0],radius*w,w)
        figure4(ax,n-1,[0,radius+radius],radius*w,w)
        figure4(ax,n-1,[0,radius-radius/w,],radius*w,w)
        ax.plot(x,y,color='k')

        
plt.close("all") 
fig, ax = plt.subplots() 
figure4(ax, 3, [0,0], 100,1/3)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('figure4.png')













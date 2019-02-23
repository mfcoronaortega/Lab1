import numpy as np
import matplotlib.pyplot as plt

def figure3(ax,n,p,w):
    if n>0:
        q = p*w
        q1 = p*w
        ax.plot(p[:,0],p[:,1],color='k')
        ax.plot(p[:,0],p[:,1],color='k')
        figure3(ax,n-1,q,q1,w)
        

plt.close("all") 
size = 3 
levels = 2
p = np.array([[-size,-size-(size/size)],[0,0],[size,-size-(size/size)]])
    
fig, ax = plt.subplots()

figure3(ax,levels,p,1/3) 

ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('figure3.png')
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import numpy as np
import numpy.random as rnd
import matplotlib.patches as patches
import matplotlib.collections as collections

#Square moving randomly over a lattice of size n
n=100
fig, ax = plt.subplots()
ax.set_xlim(-0.5,n-0.5)
ax.set_ylim(-0.5,n-0.5)

#Definition of the lattice
x = np.arange(0,n)
y = np.arange(0,n)
z = lambda x: 3*np.exp(-0.007*((x[0]-n/4)**2+(x[1]-3*n/4)**2))+2*np.exp(-0.0003*((x[0]-3*n/4)**2+(x[1]-n/4)**2)) 
convex = [[z([i,j]) for i in x] for j in y]
#Anything plotted before the animation is not deleted
#so we plot the lattice
background = ax.imshow(convex, animated = True)


ims = [] #list of frames
x=rnd.randint(0,n-1)
y=rnd.randint(0,n-1)
b = 0.01
for j in range(10): #number of increments of beta
    for i in range(300):#number of metropolis timesteps
        x_new = (x+rnd.randint(-1,2))%n 
        y_new = (y+rnd.randint(-1,2))%n
        #metropolis accepting rule
        inc_e = z([x_new, y_new])- z([x, y])
        p = 0 if b==0 else min(1,np.exp(inc_e*b)) 
        if p > rnd.rand():
            x = x_new
            y = y_new
        rect = patches.Rectangle((x-0.5,y-0.5), 1, 1, edgecolor = 'r', facecolor='r', animated = True)
        im = ax.add_artist(rect) #this is the key. Patches need to be added like this
        ims.append([im]) #alternatively [im]->[im, backgroud] or any other artists on this frame
    
    b*=2.2

anim = animation.ArtistAnimation(fig, ims, interval=300, repeat=True, blit=False)
anim.save('square_moving.mp4', fps = 60, extra_args=['-vcodec','libx264'])
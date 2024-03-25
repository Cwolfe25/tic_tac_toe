import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import math
"""
variables:
x = int
opx = int
dist = int
y = int
G = int
mH = int
mH2 = int
vx = int
vy = int
opvx = int
opvy = int
div = int
opdiv = int
aax = int
aay = int
opax = int
opay = int
inter = int
data = list
opdata = list
What they do:
these variables are origionally set but later updataed through the animaiton function
x is the x position of the first planet
y is the y position of the first planet
vx is the velocity in the x direction
vy is the velocity in the y direction
div is the part that is divided from the acceleration function
aax is the acceleration in the x
aay is hte acceleration in the y
data is where these numbers are stored between interations
all of the varibales with an op in the front is the same as the ones for the first planet but in the opposite direction
mH is the mass of hte first planet
mH2 is hte mass of the second planet
inter is the intervals which can speed up or slow down the animiation
G is hte graviety constant
"""
# Define the figure and axis
fig, ax = plt.subplots()

# Define the ellipse parameters
#Note this assumes the center of gravity is siuated at the origin

x = 500000000                      #first distance from the center of gravity
opx = -500000000                        #second distance
dist = x - opx

y = 0                              #for simplicity both stars start on the x axis
opy = y

G = 6.67*10**-11                  #gravity constant

mH = 5.97*10**29                #masses of the stars
mH2 = 5.97*10**29

vx = 0 
vy = 300000                        #intial velocities for first star

opvx = vx * -1                     #this makes them the same but can be changed
opvy = -1 * vy

div = x**2 + y**2                 #gets the bottom of the acceleration equation
div = div **1.5
opdiv = opx**2 + opy**2             
opdiv = opdiv **1.5

aax = -1 * G*mH *x / div          #acceleration of the x
aay = -1 * G *mH*y/div            #accleration of the y

opax = -1 * G *mH2*opx/opdiv        #finds them for the other planet
opay = -1 * G *mH2*opy/opdiv

# Define the animation function
inter = 10
data = [vx,vy,x,y,aax,aay,inter]              #takes the initial conditions into lists
opdata = [opvx,opvy,opx,opy,opax,opay,inter]


def animate(i):
# Clear the axis for each iteration
    ax.clear()
    inter= data[6]                      #takes the data from the lists out

    aax = data[4]
    aay = data[5]

    vx = data[0]
    vy = data[1]

    vx = 1 * vx + aax * inter                       #uses the acceleration of the x times the interval to get a new acceration
    vy = 1 * vy + aay * inter                       #NEEDS TO BE MINUES BC ITS WEIRD

    data[0] = vx                                #sets them into the data
    data[1] = vy




    x = data[2]
    yzor = data[3]


    x = x + vx * inter                          #uses velocity to find the x and y positions
    yzor = yzor + vy * inter 





    data[2] = x
    data[3] = yzor


    div = x**2 + yzor**2
    div = div **1.5

    aax = -1 * mH*G*x / div                     #finds the new acceleration
    aay = -1 * mH*G*yzor / div

    data[4] = aax
    data[5] = aay



    ax.plot(x,yzor,'ro')                    #plots the cordinets

    
    opax = opdata[4]
    opay = opdata[5]


    opvx = opdata[0]
    opvy = opdata[1]


    opvx = 1 * opvx + opax * inter                       #uses the acceleration of the x times the interval to get a new velocity
    opvy = 1 * opvy + opay * inter                       #NEEDS TO BE MINUES BC ITS WEIRD


    opdata[0] = opvx                                #sets them into the data
    opdata[1] = opvy


    opx = opdata[2]
    opy = opdata[3]


    opx = opx + opvx * inter                          #uses the velocity to find the x and y 
    opy = opy + opvy * inter 
    opdata[2] = opx
    opdata[3] = opy
    opdiv = opx**2 + opy**2
    opdiv = opdiv **1.5


    opax = -1 * mH2*G*opx / opdiv                     #finds the new acceleration
    opay = -1 * mH2*G*opy / opdiv

    opdata[4] = opax
    opdata[5] = opay
    # Plot the ellipse
    ax.plot(opx, opy, 'ro')                      #plots the cordinates
    



    # Set the axis limits
    ax.set_xlim(-5 * 10**9, 5 *10**9)                  #sets the veiwing window
    ax.set_ylim(-5 * 10**9, 5 * 10**9)

# Call the animation function and display the animation
ani = animation.FuncAnimation(fig, animate, frames=500, interval=inter)            #the frames that make it equal to 2pi is a full circle 

plt.show()
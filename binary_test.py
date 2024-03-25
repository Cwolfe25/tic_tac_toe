import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import math

# Define the figure and axis
fig, ax = plt.subplots()

# Define the ellipse parameters
"""
a = 400000
b = 200000

c = a**2 - b**2
c = abs(c)
c = math.sqrt(c)
print(c)
"""

x0 = 1000000000                      #distnace from the earth
opx = -500000000
dist = x0 - opx 
y0 = 0
opy = y0
G = 6.67*10**-11                    #gravity constant
print(G)
mH = 5.97*10**30                #mass of the planet
mH2 = 5.97*10**30
print(mH)
#formulas
#div = x**2 + y**2
#div = div **1.5
#aax = -1 * mH*G*a / div
#aay = mH*G*b / div
#vx = vx + ax * i
#vy = vy + ax * i 
#x = x + vx * i
#y = y + vy * i 
#center of mass equation
vx0 = 0 
vy0 = 300000                        #intial velocities
opvx = vx0 * -1
opvy = -1 * vy0
div = x0**2 + y0**2                 #gets the bottom of the acceleration equation
div = div **1.5
opdiv = opx**2 + opy**2
opdiv = opdiv **1.5
print(div)
aax0 = -1 * G*mH *x0 / div          #acceleration of the x
aax0 = 1 * aax0
aay0 = -1 * G *mH*y0/div            #accleration of the y
opax = -1 * G *mH2*opx/opdiv
opay = -1 * G *mH2*opy/opdiv
print(aay0)
# Define the animation function
inter = 10
data = [vx0,vy0,x0,y0,aax0,aay0,inter]              #takes the initial conditions
opdata = [opvx,opvy,opx,opy,opax,opay,inter]
print(data)
print(opdata)

def animate(i):
# Clear the axis for each iteration
    ax.clear()
    inter= data[6]

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


    x = x + vx * inter                          #uses the velocity to find the x and y 
    yzor = yzor + vy * inter 





    data[2] = x
    data[3] = yzor


    div = x**2 + yzor**2
    div = div **1.5

    aax = -1 * mH*G*x / div                     #finds the new acceleration
    aay = -1 * mH*G*yzor / div

    data[4] = aax
    data[5] = aay



    ax.plot(x,yzor,'ro')
    #ax.plot(opx, opy, 'ro')                      #plots the cordinates
    
    opax = opdata[4]
    opay = opdata[5]


    opvx = opdata[0]
    opvy = opdata[1]


    opvx = 1 * opvx + opax * inter                       #uses the acceleration of the x times the interval to get a new acceration
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
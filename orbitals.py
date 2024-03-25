import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import math
from _csv import writer

# Define the figure and axis
fig, ax = plt.subplots()
# Define the ellipse parameters
x0 = 2000000                        #distnace from the earth
y0 = 0

G = 6.67*10**-11                    #gravity constant
mH = 5.97*10**24                    #mass of the planet

vx0 = 0 
vy0 = 15000                          #intial velocities

div = x0**2 + y0**2                 #gets the bottom of the acceleration equation
div = div **1.5

aax0 = -1 * G*mH *x0 / div          #acceleration of the x
aay0 = -1 * G *mH*y0/div            #accleration of the y

# Define the animation function
inter = 1
it = 0                              #this was included for the kepler proof
data = [vx0,vy0,x0,y0,aax0,aay0,inter,it]              #takes the initial conditions in a list

def animate(i):
# Clear the axis for each iteration
    ax.clear()
    inter= data[6]
    aax = data[4]
    aay = data[5]
    vx = data[0]
    vy = data[1]

    vx = vx + aax * inter                       #uses the acceleration of the x times the interval to get a new acceration
    vy = vy - aay * inter                       #NEEDS TO BE MINUES BC ITS WEIRD

    data[0] = vx                                #redefines data
    data[1] = vy

    x = data[2]
    yzor = data[3]

    x = x + vx * inter                          #uses the velocity to find the x and y positions
    yzor = yzor + vy * inter 

    data[2] = x
    data[3] = yzor

    div = x**2 + yzor**2
    div = div **1.5
    aax = -1 * mH*G*x / div                     #finds the new accelerations
    aay = 1 * mH*G*yzor / div

    data[4] = aax
    data[5] = aay

    # Plot the ellipse
    ax.plot(x, yzor, 'ro')                      #plots the cordinates
    t = data[7]
    t = t +inter
    data[7] = t
    print(yzor)
    print(t)
    #bellow is the code I used to create the planet csv file
    """
    with open("planet.csv","a", newline = "")as add:
        csv = [t,x,yzor]
        enter = writer(add)
        enter.writerow(csv)
        add.close()
    """

    # Set the axis limits
    ax.set_xlim(-10**7, 10**7)                  #sets the veiwing window
    ax.set_ylim(-10**7, 10**7)
    ax.plot(0,0, '-ro')

# Call the animation function and display the animation
ani = animation.FuncAnimation(fig, animate, frames=500, interval=inter)            #the frames that make it equal to 2pi is a full circle 

plt.show()
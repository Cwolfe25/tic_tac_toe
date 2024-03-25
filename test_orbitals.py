import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import math
from _csv import writer

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
x0 = 5500000                        #distnace from the earth
y0 = 0
G = 6.67*10**-11                    #gravity constant
print(G)
mH = 5.97*10**24                    #mass of the planet
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
vx0 = 0 
vy0 = 8500                          #intial velocities
div = x0**2 + y0**2                 #gets the bottom of the acceleration equation
div = div **1.5
print(div)
aax0 = -1 * G*mH *x0 / div          #acceleration of the x
print("x accel")
print(aax0)
aay0 = -1 * G *mH*y0/div            #accleration of the y
print(aay0)
# Define the animation function
inter = 1
it = 0
data = [vx0,vy0,x0,y0,aax0,aay0,inter,it]              #takes the initial conditions

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
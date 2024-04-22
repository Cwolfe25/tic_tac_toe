import math 
from polynomial import polynomial
import matplotlib.pyplot as plt
gravity = -9.8
degree = input("what do you want the launch degree to be? ")
launchv = input("what do you want the lauch velocity to be? ")
displacementy = 0 
degree = float(degree)
launchv = float(launchv)
yv = math.sin(degree)
yv = abs(yv)
yv = yv * launchv
xv = math.cos(degree)
xv = abs(xv)
xv = xv * launchv
equation = [-9.8, yv, 0]
eqx = [xv,0]
flightx = polynomial(eqx)
flight = polynomial(equation)
time = yv / 9.8
print(time)
#time = math.sqrt(time)
displacementx = xv * time
print(displacementx)
count = 0

plotint = .01
x = [count]
y = [flight.plugin(count)]
while count <= time:
    count = count + plotint
        
    x.append(flightx.plugin(count))
    y.append(flight.plugin(count))
plt.plot(x, y)
plt.show()
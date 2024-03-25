from polynomial import polynomial
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
coeff = [1,2,3]
poly1 = polynomial(coeff)
interval = 1
ranmin = 0
ranmax = 5
fig, ax = plt.subplots()
ax.plot([0, 10],[0, 10])

ran = (ranmin,ranmax)
#poly1.plot(ran)
counter = ranmin
print(poly1.plugin(1))
total = 0 
while counter != ranmax:
    temp = poly1.plugin(counter)
    temp = temp * interval
    
    
    ax.add_patch(Rectangle((counter,0),interval,temp))
    counter = counter + interval
    total = total + temp
print(total)
x = [i for i in range(ran[0], ran[1])]
y = [poly1.plugin(i) for i in x]
plt.plot(x, y)
plt.show()
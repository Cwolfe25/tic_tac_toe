from polynomial import polynomial
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
coeff = [1,2,3,4,5]                                 #creates a poly nomial that would be x^2 + 2x + 3
poly1 = polynomial(coeff)
interval = 1                                    #interval used for each sum
ranmin = 0                                      #maximum and minimum of the range of the sum
ranmax = 5
fig, ax = plt.subplots()                        #creates the plot

choice = input("do you want a left, right, midpoint, or trapazoid(use l,r,m,t respectively)")
ran = (ranmin,ranmax + 1)
#left
counter = ranmin
total = 0 
if choice == "l":
    while counter != ranmax:                    #makes it so its a left sum
        temp = poly1.plugin(counter)
        checkup = counter + interval
        
        
        ax.add_patch(Rectangle((counter,0),interval,temp, alpha = .5))
        linex = [counter,checkup,checkup,counter,counter]
        liney = [0,0,temp,temp,0]
        plt.plot(linex, liney)
        counter = counter + interval
        temp = temp * interval
        total = total + temp
    print(total)
    x = [i for i in range(ran[0], ran[1])]
    y = [poly1.plugin(i) for i in x]
elif choice == "r":
    counter = counter + interval
    rightmax = ranmax + interval
    check = 0 
    while counter != rightmax:
        temp = poly1.plugin(counter)
        checkup = counter- interval
        
        ax.add_patch(Rectangle((check,0),interval,temp))
        linex = [counter,checkup,checkup,counter,counter]
        liney = [0,0,temp,temp,0]
        plt.plot(linex, liney)
        counter = counter + interval
        check = check + interval
        temp = temp * interval
        total = total + temp
    print(total)
    x = [i for i in range(ran[0], ran[1])]
    y = [poly1.plugin(i) for i in x]
elif choice == "m":
    mid = interval / 2
    counter = counter + mid
    rightmax = ranmax
    check = 0 
    while counter <= rightmax:
        temp = poly1.plugin(counter)
        checkup = counter + mid
        opcheck = counter - mid
        
        ax.add_patch(Rectangle((check,0),interval,temp))
        linex = [opcheck,checkup,checkup,opcheck,opcheck]
        liney = [0,0,temp,temp,0]
        plt.plot(linex, liney)
        counter = counter + interval
        check = check + interval
        temp = temp * interval
        total = total + temp
    print(total)
    x = [i for i in range(ran[0], ran[1])]
    y = [poly1.plugin(i) for i in x]
elif choice == "t":
    check = counter + interval
    while counter != ranmax:
        temp = poly1.plugin(counter) + poly1.plugin(check)
        temp = temp * .5 * interval
        maxup = poly1.plugin(check)
        mini = poly1.plugin(counter)
        linex = [counter,check,check,counter,counter]
        liney = [0,0,maxup,mini,0]
        plt.plot(linex, liney)
        counter = counter + interval
        check = check + interval
        total = total + temp
    print(total)

    x = [i for i in range(ran[0], ran[1])]
    y = [poly1.plugin(i) for i in x]
anti = poly1.antiderivative()
print(anti)
plt.plot(x, y)
plt.show()
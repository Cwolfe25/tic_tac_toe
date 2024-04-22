from polynomial import polynomial
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
def main():
    """
    this finds the left, right, midpoint, and trapazoid sums for a user defined polynomial 
    degree = int: this is the degree of the polynomial
    coeff = list: this is for the coeffiecntes of the polynomial
    value = float/int: this is the storage place for the coefficents 
    poly1 = polynomial: this is where the polynomial is stored
    subdiv = int: number of subdivisions
    ranmin = float: low end of the area being looked at
    ranmax = float: highend of the area being looked at
    length = float: length of the function
    interval = float: length of each interval
    choice = str: asks user what rienman they want
    counter = float: keeps track of position through the for loops
    total = float: this is the total area
    temp = float: stores the y value
    checkup = float: keeps the right boundy
    linex = list: x points for the box
    liney = list: y points for hte boxes
    
    """
    degree = input("what degree polynomial do you what?")
    degree = int(degree)                                                #asks for the degree of their polynomial
    coeff = []                                                          #for the polynomial class
    while degree >= 0:
        value = input("what do you want this value to be? ")            #for loop to define the polynomial of choice
        value = float(value)
        if value == int(value):                                         #converts to int if possible bc it looks nicer
            value = int(value)
        coeff.append(value)
        print(coeff)
        degree = degree - 1
                                   
    poly1 = polynomial(coeff)
    subdiv = input("how many subdivisions do you want? ")
    subdiv = int(subdiv)                                                #number of subdivisions

    ranmin = input("what do you want the lower boundry to be? ")        #maximum and minimum of the range of the sum
    ranmax = input("what do you want the upper boundry to be? ")
    ranmin = float(ranmin)
    ranmax = float(ranmax)
    length = ranmax - ranmin                                            #defines the length of the intervals
    interval = length / subdiv


    choice = input("do you want a left, right, midpoint, or trapazoid(use l,r,m,t respectively)")

    counter = ranmin
    total = 0 

    if choice == "l":
        while counter != ranmax:                                        #left reinmansum
            temp = poly1.plugin(counter)                                #finds the left point
            checkup = counter + interval
            linex = [counter,checkup,checkup,counter,counter]           #creates lines for the boxes
            liney = [0,0,temp,temp,0]
            plt.plot(linex, liney)
            counter = counter + interval

            temp = temp * interval                                      #finds each area
            
            total = total + temp
        print("area:")
        print(total)

    elif choice == "r":                                                 #right reinman sum
        counter = counter + interval                                    #makes it so it works for the right
        
        rightmax = ranmax + interval
        check = 0 
        while counter != rightmax:                                      #does the area calcuations and maeks the boxes for each one
            temp = poly1.plugin(counter)
            checkup = counter- interval
            
            linex = [counter,checkup,checkup,counter,counter]
            liney = [0,0,temp,temp,0]
            plt.plot(linex, liney)
            counter = counter + interval
            check = check + interval
            temp = temp * interval
            total = total + temp
        print("area")
        print(total)

    elif choice == "m":                                                 #does the midpoint sum
        mid = interval / 2                                              #makes it so it can find the mid point
        counter = counter + mid
        rightmax = ranmax
        check = 0 
        while counter <= rightmax:                                      #makes the boxes for each midpoint and graphs it
            temp = poly1.plugin(counter)
            checkup = counter + mid                                     
            opcheck = counter - mid
            

            linex = [opcheck,checkup,checkup,opcheck,opcheck]
            liney = [0,0,temp,temp,0]
            plt.plot(linex, liney)
            counter = counter + interval
            check = check + interval
            temp = temp * interval
            total = total + temp
        print("area")
        print(total)

    elif choice == "t":                                                 #does trapazoid
        check = counter + interval
        while counter != ranmax:
            temp = poly1.plugin(counter) + poly1.plugin(check)          #creates gets the trapazoid area and the trapazoids to cover them
            temp = temp * .5 * interval
            maxup = poly1.plugin(check)
            mini = poly1.plugin(counter)
            linex = [counter,check,check,counter,counter]
            liney = [0,0,maxup,mini,0]
            plt.plot(linex, liney)
            counter = counter + interval
            check = check + interval
            total = total + temp
        print("area")
        print(total)
    count = ranmin

    plotint = .01                                                       #creates an acurate graph by going through the x and y values
    x = [count]
    y = [poly1.plugin(count)]



    while count <= ranmax:
        
        count = count + plotint
        
        x.append(count)
        y.append(poly1.plugin(count))

    plt.plot(x, y)
    plt.show()
    anti = antidiv(coeff)                                               #finds the antiderivative
    anticoeff = polynomial(anti)
    
    area = anticoeff.plugin(ranmax) - anticoeff.plugin(ranmin)          #gets the integral
    
    if area == 0:                                                       #makes sure its not undefined
        error = total - area
        error = error * 100
        error = abs(error)
    else:                                                               #finds the percent error
        error = total - area
        error = error / area
        error = abs(error)
        error = error * 100
    print("precent error:")
    print(error)
def antidiv(coeffs):
    """
    this function finds the anti derivative
    takes: 
    coeffs -list
    returns:
    anticoff - list
    Local variables:
    degree = int: this is the degree of the polynomial
    anticoff = list: where the anti derivitive is stored
    otherdeg = int: this balences the first degree to make the for loop work
    op = float: this is a part of the anti process which balences out the degree
    """
    degree = len(coeffs)                                    #takes the degree of the polynomial for the for loop
    anticoff = []
    otherdeg = 0
    while degree >= 1:                                      #goes through each degree number in decending order and accendign order for otherdeg
        if coeffs[otherdeg] == 0:                           #checks to see if the degree is 0 so it doesnt return anthing undefined
            anticoff.append(0)
            degree = degree - 1
            otherdeg = otherdeg + 1
        else:                                               #anti-differntiates
            op = 1/degree
            temp = coeffs[otherdeg] * op                    #finds the front coefficent
            anticoff.append(temp)
            degree = degree - 1
            otherdeg = otherdeg + 1
    anticoff.append(0)                                      #adds the extra value at the end
    
    return(anticoff)
if __name__ == "__main__":
    main()
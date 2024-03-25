"""
for this proof the distances between the first foci point(the host planet at the origion) and hte second foci point should be the same for every iteration
file = csv file
line = list
x1 = float
y1 = float
d1 float 
d2 float
a2 = float
"""
import math
file = open("planet.csv")                           #planet.csv is a file i made htat stores an interation of a planet cycle from my orbitals assignment
for line in file:
    line = line.split(",")                          #the csv is split into iteration, x position, y position
    print(line)
    x1 = line[1]                                    #takes the positions out of the list
    y1 = line[2]
    x1 = float(x1)                                  #converts it to a float
    y1 = float(y1)
    d1 = x1**2 + y1 **2
    d1 = math.sqrt(d1)                              #first distance by using distance formula
    d2 = x1 - 2105083                               #first the other foci point
    d2 = d2 ** 2 
    d2 = d2 + y1 **2                                #uses distance formula again with the other foci point
    d2 = math.sqrt(d2)
    a2 = d1 + d2                                    #adds them togeather
    # a2 should be around 5894917
    print(a2)                                       #the proof works within an acceptable marigin on error
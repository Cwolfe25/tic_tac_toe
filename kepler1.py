import math
file = open("planet.csv")
for line in file:
    line = line.split(",")
    print(line)
    x1 = line[1]
    y1 = line[2]
    x1 = float(x1)
    y1 = float(y1)
    d1 = x1**2 + y1 **2
    d1 = math.sqrt(d1)
    d2 = x1 - 2105083
    d2 = d2 ** 2 
    d2 = d2 + y1 **2
    d2 = math.sqrt(d2)
    a2 = d1 + d2
    # a2 should be around 5894917
    print(a2)
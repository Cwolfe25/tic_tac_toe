'''
Created on Apr 3, 2023

@author: CWolfe25
variable
file = file
d = dictionary
words = str
tup = tuple
'''
def main():
    try:
        file = open("tuple.txt",'r')                       #opens the file and reports if it can't open it
        print(file)
    except:
        print('File cannot be opened:')
        exit()
    d = dict()                                              #creates a dictionary to store the values
    for line in file:
        words = line.split()                                #goes through each line of the file
        if "From:" in line:
            for line in words:                              #takes the lines that have from: in it and add them into the dictionary
                if line not in d:
                    d[line] = 1
                else:
                    d[line] +=1
    
   
    lst = []                                                #creates a list
    print(d)
    for key, value in d.items():                            #goes through all of the dict values and adds them into a list
        if key != "From:":                                  #gets rid of the from
            value = str(value)
            enter = (value,key)                             #reverses it
            lst.append(enter)                               #adds it
    tup = tuple(lst)                                        #convert to a tuple
    tup = sorted(tup)                                       #sorts it
    
    
    print(tup)
    most = max(tup)                                         #prints the highest one
    print(most)
    
    
    
    
    
        

if __name__ == "__main__":
    main()
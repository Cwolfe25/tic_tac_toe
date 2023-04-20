'''
Created on Apr 10, 2023

@author: CWolfe25
file = file
file is the file where I get the words from
d is a dictionary
d takes all the lines that have "From:" in it
key an str
key is the letter
value = str
value is the number of occurences
lst = list
lst stores the hours
d2 is a dictionary 
d2 takes all the hours and gets their occurences
tup is a tuple
it stores the hour and number of occurences then sorts it
'''
def main():
    print("ok")
    try:
        file = open("tuple.txt",'r')                       #opens the file and reports if it can't open it
        print(file)
    except:
        print('File cannot be opened:')
        exit()
    d = dict()
    for line in file:
        words = line.split()                                #goes through each line of the file and adds all lines with From:
        if "From" in line:
            for line in words:                              
                if line not in d:
                    d[line] = 1
                else:
                    d[line] +=1
    print(d)
    lst = []
    for key, value in d.items():                            #gets rid of the from and only gets the time and puts in in a list
        index = key.find(":")
        if index != -1 and key != "From:":
            value = str(value)
            key = key[0:2]
            enter = (key)                            
            lst.append(enter)  
        else:
            pass  
    print(lst)
    d2 = dict()
    for value in lst:                                       #gets the times an occurences
        if value not in d2:
            d2[value] = 1
        else:
            d2[value] += 1
    print(d2)
    
    lst2 = []
    for key, value in d2.items():                           #converts to a list
        value = str(value)
        enter = (key,value)
        lst2.append(enter)
    print(lst2)
    tup = tuple(lst2)                                       #converts to a tuple
    tup = sorted(tup)                                       #sorts it
    prinz(tup)
    
        
def prinz(tup):
    """
    takes tup
    returns none
    variables
    tup = tuple
    """
    for value in tup:                                       #prints all the values individualy 
        print(value)




if __name__ == '__main__':
    main()
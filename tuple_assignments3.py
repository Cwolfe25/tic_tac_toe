'''
Created on Apr 19, 2023

@author: CWolfe25
variables
file = file
lst = list
line = str
linez = str
lst2 = list
lst 3 = list
lst4 = list
d = dictionary
counter = int
'''

def main():
    try:
        file = open("tuple.txt",'r')                       #opens the file and reports if it can't open it
        print(file)
    except:
        print('File cannot be opened:')
        exit()
    lst = []                                                # takes all of the words in the file and puts them into a list
    for line in file:
        linz = line.split()
        for line in linz:
            lst.append(line)
    lst2 = []                                               #converts all of the words into lists of thier letters
    print(lst[0])
    for letter in lst:
        letterz = list(letter)
        lst2.append(letterz)
    print(lst2[0])
    lst3 = []                                               #takes all of the letters and puts them into a list
    for letter in lst2:
        counter = len(letter) - 1
        if counter >= 0:
            lst3.append(letter[counter])
            counter = counter - 1
            

    d = dict()                                              #takes all of the letters and finds their occurence
    for letter in lst3:
        letter = letter.lower()
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
    lst4 = []
    for key, value in d.items():                            #only takes the real letters and puts them into a list
        if key == "a" or key == "b" or key == "c" or key == "d" or key == "e" or key == "f" or key == "g" or key == "h" or key == "i" or key == "j" or key == "k" or key == "l" or key == "m" or key == "p" or key == "q" or key == "r" or key == "s" or key == "t" or key == "u" or key == "v" or key == "w" or key == "x" or key == "y" or key == "z":
            value = str(value)
            enter = (key,value)                            
            lst4.append(enter)
    tup = tuple(lst4)                                       #converts to a tuple, sorts, and prints it
    tup = sorted(tup)
    print(tup)
            
        
if __name__ == '__main__':
    main()
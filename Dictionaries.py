'''
Created on Mar 2, 2023

@author: CWolfe25
variables
file1 is a file that is opened and then looked through for work occurence
bee is a dictionary that takes all the words and their occurence in file2
words splits the file
word is any word in the file and is a string
output1 is a file that is created as a csv


'''

def main():
    print("ok")
    try:
        file1 = open("Bee_Movie.txt",'r')                       #opens the file and reports if it can't open it
        print(file1)
    except:
        print('File cannot be opened:')
        exit()
            
    Bee = dict()                                                #creates an empty dictionary
    for line in file1:
        words = line.split()
        for word in words:                                      #looks through the file finds all words and their occurence
            if word not in Bee:
                Bee[word] = 1
            else:
                Bee[word] += 1
    print("Bee Movie Word Appearance:")        
    for key,value in Bee.items():                               #adds every word its occurence into the dictionary
        print(key + ' ' + str(value))
        
    output = open("Bee_Movie.csv","w")                          #creates a csv and adds every words and its occurence
    for key, value in Bee.items():
        if value > 20:
            output.write(key + "," + str(value) + "\n")
    
    file1.close()
if __name__ == '__main__':
    main()

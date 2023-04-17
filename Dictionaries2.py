'''
Created on Mar 19, 2023

@author: CWolfe25
'''

def main():
    try:                                                #tries to open the text file and reports if it doesn't work
        file2 = open("Ferris.txt",'r')
    except:
        print('File cannot be opened:')
        exit()
            
    south = dict()                                      #creates an empty dictionary
    for line in file2:
        words = line.split()
        for word in words:
            if word not in south:
                south[word] = 1
            else:
                south[word] += 1
            
    for key,value in south.items():
        print(key + ' ' + str(value))
        
    output2 = open("Ferris.csv","w")
    print("ok")
    for key, value in south.items():
        if value > 20:
            output2.write(key + "," + str(value) + "\n")
            print("yes")
if __name__ == '__main__':
    main()
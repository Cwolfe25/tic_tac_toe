#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'decodeMessage' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING text
#  2. STRING message
#

def decodeMessage(text, message):
    # Write your code here
    print(message)
    message1 = message.split(" ")
    finalword = []

    for value in message1:
        value1 = value.split(".")
        sentance = value1[0]
        sentance = int(sentance)
        
        word = value1[1]
        word = int(word)
        
        letter = value1[2]
        letter = int(letter)
        
        sentance = sentance - 1
        letter = letter -1
        word = word - 1
        
        text1 = text.split(".  ")
        plen = len(text1)
        plen = plen - 1
        if plen >= sentance:
            sentance1 = text1[sentance]
            print(sentance1)
            sentance2 = sentance1.split(" ")
            sentlen = len(sentance2)
            sentlen = sentlen - 1
            if sentlen >= word:
                word1 = sentance2[word]
                check = 0
                alph = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890"
                alph.split()
                com = len(word1)
                com = com - 1
                for character in alph:
                    if word1[0] == character:
                        check = 1
                if check == 0:
                    leng = len(word1)
                    leng = leng -1
                    wordtemp = []
                    check = 1
                    while check <= leng:
                        wordtemp.append(word1[check])
                        check = check + 1
                    word1 = wordtemp
                wrdlen = len(word1)
                wrdlen = wrdlen - 1
                print(word1)
                if wrdlen >= letter:
                    letter2 = word1[letter]
                else:
                    letter2 = " "
            else:
                letter2 = " "
        else:
            letter2 = " "
        print(letter2)
        finalword.append(letter2)
    print(finalword)
    sep = ""
    result = sep.join(finalword)

        
    """
    for char in finalword2:
        if char =="," or char == "'":
    """
    return(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text = input()

    message = input()

    result = decodeMessage(text, message)

    fptr.write(result + '\n')

    fptr.close()

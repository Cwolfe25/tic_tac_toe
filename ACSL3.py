#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'playRackO' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING info
#  2. STRING rack
#  3. STRING pile
#

def playRackO(info, rack, pile):
    # Write your code here
    infotemp = info.split(" ")
    rackstack = rack.split(" ")
    pilestack = pile.split(" ")
    done = 0
    pilecounter = 0
    if int(infotemp[0])== len(rackstack):
        while done == 0:
            for value in pilestack:
                
                temp = rule1(rackstack, value)
                rackstack = temp[0]
                stoper = temp[1]
                
                if stoper == 0:
                    
                    temp = rule2(rackstack, value)
                    rackstack = temp[0]
                    stoper = int(temp[1])
                    if stoper == 0:
                        temp = rule3(rackstack, value)
                        rackstack = temp[0]
                        stoper = int(temp[1])
                        if stoper == 0:
                            temp = rule4(rackstack, value)
                            rackstack = temp[0]
                            stoper = int(temp[1])
                            if stoper == 0:
                                temp = rule5(rackstack, value)
                                rackstack = temp[0]
                                stoper = int(temp[1])
                
                
                done = check(rackstack)
                print(done)
                if done ==0:
                    print(rackstack)
                    answer = summation(rackstack)
                    return answer
               
def rule1(rackstack, value):
    counter = 0
    stoper = 0
    value = int(value)
    for card in rackstack:
        card = int(card)
        tempval = value + 1
        
        if tempval == card and counter != 0:
            tempcounter = counter - 1
            rackstack[tempcounter] = value
            
            print("passes rule 1")
            stoper = stoper + 1
            break
        counter = counter + 1
    return rackstack, stoper
def rule2(rackstack, value):
    counter = 0
    stoper = 0
    value = int(value)
    for card in rackstack:
        card = int(card)
        bigv = value - 1
        if bigv == card and counter != len(rackstack)-1:
            tempcounter = counter + 1
            print(tempcounter)
            rackstack[tempcounter] = value
            
            print("passes rule 2")
            stoper = stoper + 1
            break
        counter = counter + 1
    return rackstack, stoper
def rule3(rackstack, value):
    counter = 0
    stoper = 0
    value= int(value)
    for card in rackstack:
        card = int(card)
        checkmid = counter + 2
        stoper = 0
        if checkmid <= len(rackstack) - 1:
            midvcard = int(rackstack[checkmid])
        else:
            midvcard = -1
        tmid = counter + 1
        stoper = 0
        if tmid <= len(rackstack) - 1:
            mid = int(rackstack[tmid])
        else:
            midvcard = -1
        j = 0
        if mid < card or mid > midvcard:
            j = j + 1
        if card < value and value < midvcard and j == 1:
            tempcounter = counter + 1
            rackstack[tempcounter] = value
            stoper = stoper + 1
            print("passes rule 3")
        counter = counter + 1
    return rackstack, stoper
def rule4(rackstack, value):
    stoper = 0
    value = int(value)
    if value < int(rackstack[1]) and int(rackstack[0])>int(rackstack[1]):
        rackstack[0] = value
        print("passes rule 4")
        stoper = stoper + 1
    return rackstack, stoper
def rule5(rackstack, value):
    stoper = 0
    value = int(value)
    if value > int(rackstack[len(rackstack)-2]) and int(rackstack[len(rackstack)-1])< int(rackstack[len(rackstack)-2]):
        rackstack[len(rackstack)-1] = value
        stoper = stoper + 1
    return rackstack, stoper
def summation(rackstack):
    counter = 0
    total = 0
    print("in")
    for value in rackstack:
        value = int(value)
        total = total + value
        c1 = counter + 1
        if c1 <= len(rackstack) - 1:
            v1 = int(rackstack[c1])
        else:
            v1 = 0
        c2 = counter + 2
        if c2 <= len(rackstack) - 1:
            v2 = int(rackstack[c2])
        else:
            v2 = 0
        
        if value + 1 == v1 and value + 2 == v2:
            total = total + 15
        counter = counter + 1
        print(total)
    return (total)
        
def check(rackstack):
    
    numb = len(rackstack)
    numb = numb - 1
    check = 1
    breaks = 0
    wincon = 0
    while check <= numb and breaks == 0:
        bigval = rackstack[check]
        smallval = rackstack[check-1]
        bigval= int(bigval)
        smallval = int(smallval)
        if smallval < bigval:
            check = check + 1
        else:
            breaks = breaks +1
    if breaks == 1:
        wincon =1

    else:
        wincon = 0
        print("yippy")
    wincon = int(wincon)
    return wincon
"""
def fail(rackstack):
    counter = 0
    failure = 0
    for value in rackstack:
        value = int(value)
        if value > int(rackstack[counter+1]):
            failure = failure - 1
        counter = counter + 1
    return failure
"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    info = input()

    rack = input()

    pile = input()

    result = playRackO(info, rack, pile)

    fptr.write(str(result) + '\n')

    fptr.close()

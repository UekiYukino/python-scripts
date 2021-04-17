#!/usr/bin/env python3

def toBin(num):
    if num==0:
        return ""

    #Extract the remainder and add to the end of the binary string
    return "{}{}".format(toBin(num//2),num%2)

myNum=int(input("Enter a number: "))
print(toBin(myNum))

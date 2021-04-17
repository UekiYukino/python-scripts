#!/usr/bin/env python3

def hexChar(num):
    if num == 10:
        return "A"
    elif num == 11:
        return "B"
    elif num == 12:
        return "C"
    elif num ==13:
        return "D"
    elif num == 14:
        return "E"
    elif num == 15:
        return "F"
    else:
        return num

def toHex(num):
    if num ==0:
        return "" 
    return "{}{}".format(hexChar(toHex(num//16)),hexChar(num%16))

myNum=int(input("Enter your number: "))
print("0x{}".format(toHex(myNum)))

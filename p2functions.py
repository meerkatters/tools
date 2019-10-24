"""
Written by Nicolette Lewis
at University of Washington
for CESG 505: Engineering Computing
Date: October 15, 2019
Homework 2
Problem 1 - baseconverter.py
Program Description:
basecheck(base,inval,pr=0):     Checks to see if the input string is a valid expression of an integer in the provided base
                                if not, changes the base of the number to the minimum possible base
to_base(newbase,inval,pr=0):    Takes the input base as an integer and the input value as a string, returns a new
                                string containing the integer and its base and an equation showing the input
decimal(inbase,inval,pr=0):
                                Takes an input base integer and a string of the integer to be converted from the specified base
                                to decimal
                                Returns both the input integer with its base and the converted integer with its base (decimal)
add(base, inval1,inval2,pr=0):
                                Takes an input base integer and a string of the integers to be added
                                converts from the specified base to decimal adds the integers in decimal
                                Converts back to the specified base and returns the sum of the two numbers in their original bases
"""

import re
import operator
# functions
##
def basecheck(base,inval,pr=0):

    if (type(inval) is str) !=True:
        print("Please input a string!")
        inval=str(inval)
    charlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    charlist1=charlist+['-']
    for x in inval:  # this is a check on the input base of the number.
        if (str(x.lower()) not in charlist1) and (str(x.upper()) not in charlist1):
            print('The program cannot return a value for {} in base {}, sorry :('.format(inval,base))
            exit

    return inval

def to_base(newbase,inval,pr=0):
    # takes an input base integer and a string of the integer to be converted to the specified base
    # returns both the input integer with its base and the converted integer with its base
    inval=basecheck(newbase,str(inval),1)
    s = decimal(newbase,str(inval))
    inval=str(inval)
    if newbase not in range(2, 17, 1):
        print("Please enter a base between 2 (binary) and 16 (hex)")
        exit()
    charlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    out=[]
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

    if inval[0] == '-':
        hold = '-'
        s=-s
    else:
        hold = ''
    while s > 0:
        rem = s % newbase
        s //= newbase
        out.insert(0, charlist[rem])

    out=''.join(out)
    out=out.upper()
    empty = ''
    if out == empty:
        out = '0'

    if pr==1:
        report = "{}{} = {}{}"
        print(report.format(inval, str(base).translate(SUB), out, str(newbase).translate(SUB)))

    return hold + out
##

def decimal(base,inval,pr=0):
    # takes an input base integer and a string of the integer to be converted from the specified base to decimal
    # returns both the input integer with its base and the converted integer with its base (decimal)
    charlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    inval=basecheck(base,inval)
    inval=str(inval)
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")     # this allows the output to be put into subscript form
    dec = 0                                             # initializing output decimal
    hold = ''                                           # initializing the sign of the output
    if inval[0] == '-':                                 # creating a conditional for the sign of the output integer
        hold = '-'
        start=1
    else:
        start=0
    for i in range(start,len(inval)):
        if (inval[i] not in charlist) and (str(inval[i]).lower() not in charlist):
            print('The requested input is not representable in bases 2 through 16')
            inval='0'*len(inval)

    if len(inval) != 1:
        for i in range(start, len(inval)):
            dec += charlist.index(str(inval[i]).lower())  * (base ** ((len(inval) - 1) - i))
    else:
        inval=str(inval).lower()
        dec += charlist.index(inval.lower()) * base ** ((len(inval) - 1))
    out = hold+str(dec).upper()


    if pr==1:
        report = "{}{} = {}{}"
        print(report.format(inval, str(base).translate(SUB), out, str(10).translate(SUB)))

    return int(out)
##
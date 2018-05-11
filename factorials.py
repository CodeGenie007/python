#!/usr/bin/python

# Calculating factorials

n = int(input(" Please Enter an integer "))
fact = 1
for i in range (2,n +1):
    fact = fact * i
print (str(n) + " factorial is " + str(fact)) 

#!/usr/bin/python

#Print Prime numbers up to...

for num in range(2,200):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
        print num        
        

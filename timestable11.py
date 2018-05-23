#!/usr/bin/python

# Times table 

for row in range(1, 11):
    for col in range(1, 11):
        prod = row * col
        if prod < 10:
            print("", end = ")
        print(row * col, "", end ="")          
    print ()       
#needs fix

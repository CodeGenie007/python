#!/usr/bin/python

import sys

print sys.argv

#print sys.argv, len(sys.argv)
if len(sys.argv) != 4:
  print "wrong number of arguments!"
  sys.exit(1)
a = sys.argv[1]
b = sys.argv[3]

op = sys.argv[2]
if op == "-":
  try:
    if a.count(".") + b.count(".")  > 0:
      print float (a) - float (b)
    else:  
      print int(a) - int(b)
  except ValueError:
    print "not a number"
if op == "+":
  try:
    if a.count(".") + b.count(".")  > 0:
      print float (a) + float (b)
    else:  
      print int(a) + int(b)
  except ValueError:
    print "not a number"
if op == "/":
  try:
    if a.count(".") + b.count(".")  > 0:
      print float (a) / float (b)
    else:  
      print int(a) / int(b)
  except ValueError:
    print "not a number"
if op == "*":
  try:
    if a.count(".") + b.count(".")  > 0:
      print float (a) * float (b)
    else:  
      print int(a) * int(b)
  except ValueError:
    print "not a number"

    


  
  

  

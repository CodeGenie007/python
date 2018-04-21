#!/usr/bin/python

import sys

#print sys.argv, len(sys.argv)
if len(sys.argv) != 3:
  print "wrong number of arguments!"
  sys.exit(1)
a = sys.argv[1]
b = sys.argv[2]

if a == b:
  print 'Equal'
else:
  print 'Non-equal'

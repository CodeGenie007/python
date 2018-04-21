#!/usr/bin/python

n = 9


def pyramid(n):       #definening a funcion name and parameters
  i = 1
  while i <= n:
    print "line", i,
    j = 1
    while i + j <= n:
      print "*",
      j = j + 1
    j = 1
    while j < i:       #prints out first half of the line ,piramide
      print j,
      j = j + 1
    j = i               # j already has the right value so this is redundant
    while j >= 1:       #prints out secont half of pyramide
      print j,
      j = j - 1
    print
    i = i + 1

for i in xrange(1,10):
  print
  print 'Pyramid', i
  pyramid(i)


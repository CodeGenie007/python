#!/usr/bin/python



def square(n):
  i = 1
  while i <= 2 * n - 1:           
    print 'line:', '%2d' % i, "->  ",
    j = 1    
    while j <= 2 * n -1:
      # distance to the closest of 4 edges
      print min(i, j, 2 * n - j, 2 * n - i),
      j += 1
    print  
    i += 1

for i in xrange(1,10):
  print
  print 'Square', i
  square(i)

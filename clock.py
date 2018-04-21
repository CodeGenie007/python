#!/usr/bin/python -u
import time

print "running"

while True:
  print time.asctime(), '\r'
  time.sleep(1)

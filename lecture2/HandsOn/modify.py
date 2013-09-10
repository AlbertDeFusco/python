#!/usr/bin/env python

def modify(x,y,z):
  x = 28
  y.append(42)
  z.append(99)
  z = [8, 99]
  print id(x),id(y),id(z)
  print x,y,z

a = 77
b = [28]
c = [8]

print id(a),id(b),id(c)
print
modify(a,b,c)

print
print id(a),id(b),id(c)
print a,b,c

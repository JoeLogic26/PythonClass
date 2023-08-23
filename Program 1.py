"""
Joseph Stallcop
CS 410P
Lab Assignment 2L

The following program does a variety of exercises in NumPy.

"""
import numpy as np
#importing numpy

import random
#importing random

print("1)", np.__version__)
#print numpy version

print()
a = np.zeros(10)
print("2)", a)
#create a null vector of size 10

print()
a[4:7] = 5
print(a)
#set the 5th through 7th value of the array to 5

print()
b = np.array(range(10,99), int)
print("3)", b)
#create an array whose elements go from 10 to 99

print()
c = np.random.randint(10, 100, size=(10))
print("4)", c)
#create an array of 10 elements with values 10 - 99

print()
d = np.array(range(0,9))
d = d.reshape((3, 3))
print("5)", d)
#create a 3x3 matrix with values from 0-8

print()
e = np.array([1,2,0,0,4,0])
print("6)", np.where(e != 0))
#initialize an array with [1,2,0,0,4,0] and find indices of non-zero elements

print()
f = np.identity(3, dtype=float)
print("7)", f)
#create a 3x3 identity matrix

print()
g = np.zeros((5,5))
print("8)", g)
#create a 5x5 matrix of zeroes

print()
g[::, 0:1:] = 5
g[4] = 5
print(g)
#change first and last row to 5's

print()
h = np.zeros((8, 8))
h[1::2, ::2] = 1
h[::2, 1::2] = 1
print("9)", h)
#create an 8x8 and fill it with a checkerboard pattern

print()
x = np.random.rand(25)
print("10)", x)
#create a random array of size 25 and call it x

print()
x = sorted(x)
print(x)
#sort x
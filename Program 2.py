"""
Joseph Stallcop
CS 410P
Lab Assignment 2L

The following program creates 2 graphs in matplotlib.

"""

import matplotlib.pyplot as plt
#imports matplotlib


xLst = []
yLst = []
#creates x and y lists
    
    
file = open('input', "r")
#opens the file
    
for line in file:
    x, y = line.split(",")
    xLst.append(float(x))
    yLst.append(float(y))
    #uses a for loop to add items from file to list in
    #stripped form
    
file.close()
#closes the file


plt.figure(1)
#creates the first figure

first = plt.plot(xLst, yLst, "-")
#puts the first plot, containing both lists and dashed line style, into a variable

plt.setp(first, color='g')
#sets the color to green

plt.ylabel("Y")
plt.xlabel("X")
#labels both axis

plt.title("Line Chart with Dashes")
#creates a title for the chart

plt.figure(2)
#creates the first figure

second = plt.plot(xLst, yLst, "o")
#puts the first plot, containing both lists and circle style, into a variable

plt.setp(second, color='r')
#sets the color to red

plt.ylabel("Y")
plt.xlabel("X")
#labels both axis

plt.title("Line Chart with Dots")
#creates a title for the chart


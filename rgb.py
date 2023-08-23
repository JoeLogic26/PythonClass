"""
Joseph Stallcop
CS 410P
Lab Assignment 2L

The following program uses red, green, and blue intensity
data for multiple colors, then displays this on a bar
graph with the use of matplotlib and numpy.

"""

import matplotlib.pyplot as plt
import numpy as np
#import matplotlib and numpy


red = [220, 255, 165, 65, 180, 238, 57, 192, 255]
green = [20, 219, 42, 224, 105, 130, 255, 192, 255]
blue = [60, 88, 42, 208, 180, 238, 20, 192, 255]
#setting up data variables


wide = 0.25
#setting bar width

fig = plt.subplots(figsize =(12, 8))
#setting the size

plt.title("RGB Values for Colors")
#creating the title
 
br1 = np.arange(len(red))
br2 = [x + wide for x in br1]
br3 = [x + wide for x in br2]
#setting the bar positions on the x axis
 
bar1 = plt.bar(br1, red, color ='r', width = wide)
bar2 = plt.bar(br2, green, color ='g', width = wide)
bar3 = plt.bar(br3, blue, color ='b', width = wide)
#plotting the data and placing it into variables, 
#with color and width inside variables
 
plt.ylabel("RGB Values")
#creating the y axis title

plt.xticks([r + wide for r in range(len(red))],
        ['crimson\n220,20,60', 'mustard\n255,219,88', 'brown\n165,42,42', 'turquoise\n65,224,208', 'pink\n180,105,180', 'violet\n238,130,238', 'neon\n57,255,20', 'silver\n192,192,192', 'white\n255,255,255'])
         #creating the titles of each section of bars
         
plt.legend((bar1[0], bar2[0], bar3[0]), ('Red', 'Green', 'Blue') )
#creating the legend

plt.show()
#outputting the graph





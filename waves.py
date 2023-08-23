"""
Joseph Stallcop
CS 410P
Lab Assignment 2L

The following program creates Sine and Cosine waves as well as
tangent values with numpy arrays, then graphs them all in 
matplotlib.

"""

import matplotlib.pyplot as plt
import numpy as np
#import matplotlib and numpy

fig = plt.figure(figsize=(10,6))
#create and size the figure


ax1 = fig.add_subplot(3, 1, 1)
#create the subplot

ax1.set_xlabel("x --> in radians")
ax1.set_ylabel("y --> sin(x)")
ax1.set_title('Sine, Cosine, and Tangent Waves \nSine Values 0 to 360 degrees repeated 4 times')
#create axis labels and title

x = np.arange(0, 8*np.pi, .1)
y = np.sin(x)
#set the x and y values

line1 = ax1.plot(x, y, color='blue', lw=1)
#plot the values in blue


ax2 = fig.add_subplot(3, 1, 2)
ax2.set_xlabel("x --> in radians")
ax2.set_ylabel("y --> cos(x)")
ax2.set_title("Cosine Values 0 to 360 degrees repeated 4 times")

x = np.arange(0, 8*np.pi, .1)
y = np.cos(x)

line2 = ax2.plot(x, y, color='red', lw=1)

ax3 = fig.add_subplot(3, 1, 3)
ax3.set_xlabel("x --> in radians")
ax3.set_ylabel("y --> tan(x)")
ax3.set_title("Tangent Values 0 to 180 degrees (excluding 90)")

x1 = np.linspace(0, 89, 100)
x2 = np.linspace(91, 180, 100)
#set the x values in degrees

rad1 = np.deg2rad(x1)
rad2 = np.deg2rad(x2)
#convert degrees to radians

y1 = np.tan(rad1)
y2 = np.tan(rad2)
#create y values from tangents of radians

line3, = ax3.plot(rad1, y1, "^", color='red')
line4, = ax3.plot(rad2, y2, "^", color='green')
#plot tangent values in red and green triangles

ax3.legend([line3, line4], ["0°-89°", "90-180°"], fontsize="8", loc="upper left")
#create a legend

fig.tight_layout()
#fits subplots to plot
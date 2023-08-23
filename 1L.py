"""
Joseph Stallcop
CS 410P
Lab Assignment 1L

This project, using the inputs of side and height length, as well as radius,
computes and outputs the area and volume of numerous figures.
"""

from math import *
#Importing the math module

side = int(input("Enter value for Side: "))
radius = int(input("\nEnter value for Radius: "))
height = int(input("\nEnter value for Height: "))
#Collecting the length of side and height, and the radius

print("\nYou entered: \nSide =", side, "\nRadius =", radius, "\nHeight =", height)
#Outputing the user input

square_area = side ** 2
print("\nArea of Square: ", square_area)
#Calculating and outputing the square area

circle_area = pi * (radius ** 2)
print("Area of Circle: ", circle_area)
#Calculating and outputing the circle area

cube_sur_area = 6 * (side ** 2)
print("Area of Cube Surface: ", cube_sur_area)
#Calculating and outputing the cube surface area

sphere_area = 4 * pi * (radius ** 2)
print("Area of Sphere: ", sphere_area)
#Calculating and outputing the sphere area

cyl_lat_sur_area = 2 * pi * radius * height
print("Area of Cylinder Lateral Surface: ", cyl_lat_sur_area)
#Calculating and outputing the cylinder lateral surface area

cone_lat_sur_area = pi * radius * side
print("Area of Cone Lateral Surface: ", cone_lat_sur_area)
#Calculating and outputing the cone lateral surface area

cube_volume = side ** 3
print("\nVolume of Cube: ", cube_volume)
#Calculating and outputing the cube volume

sphere_volume = (4/3) * pi * (radius ** 3)
print("Volume of Sphere: ", sphere_volume) 
#Calculating and outputing the sphere volume

cylinder_volume = pi * (radius ** 2) * height
print("Volume of Cylinder: ", cylinder_volume)
#Calculating and outputing the cylinder volume

cone_volume = (1/3) * pi * (radius ** 2) * height
print("Volume of Cone: ", cone_volume)
#Calculating and outputing the cone volume
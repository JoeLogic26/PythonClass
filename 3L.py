"""
Joseph Stallcop
CS 410P
Lab Assignment 2L

The following program takes user input of two coordinates, then outputs 
which section of the Cartesian plane they would be on.

"""

x = float(input("Enter X Coordinate: "))
y = float(input("\nEnter Y Coordinate: "))
#takes user input of X and Y coordinate, converts them into float, 
#then places them into variables x and y

if x > 0 and y > 0:
    location = "Quadrant 1"
elif x < 0 and y > 0:
    location = "Quadrant 2"
elif x < 0 and y < 0:
    location = "Quadrant 3"
elif x > 0 and y < 0:
    location = "Quadrant 4"
elif x == 0 and y != 0:
    location = "Y Axis"
elif x != 0 and y == 0:
    location = "X Axis"
elif x == 0 and y == 0:
    location = "Origin"
#Determines location of coordinates with use of else, elif, and 
#the and statement

print("\nCoordinates:", x, ",", y)
print("\nCoordinates Location:", location)
#outputs the user coordinates in an organized way, then outputs the
#location of the coordinates
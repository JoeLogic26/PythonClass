"""
Joseph Stallcop
CS 410P
Lab Assignment 2L

The following program takes a series of two sets of coordinates seperated 
by a space, outputs them in a list format, then outputs where 
their location is, as well as the distances between them.

"""

from math import *
#imports math function

def where_is_xy(items):
#sets up the location finding function

    x = items[0]
    y = items [1]
    #takes input of a tuple and splits it into variables
   
    if x > 0 and y > 0:
       location = "Quadrant 1"
    elif x < 0 and y > 0:
       location = "Quadrant 2"
    elif x < 0 and y < 0:
       location = "Quadrant 3"
    elif x > 0 and y < 0:
       location = "Quadrant 4"
    elif x == 0 and y != 0:
       location = "Y-Axis"
    elif x != 0 and y == 0:
       location = "X-Axis"
    elif x == 0 and y == 0:
       location = "Origin"
    #finds the location of a set of coordinates
    
    return(location)
    #returns the location of a set of coordinates
    
    

def main():
#sets up the main function

    cont = True
    #sets up the first while loop
    coordinateList = []
    #creates the coordinate list
    
    while cont == True:
    #creates the first while loop
    
            coordinates = input("Enter X and Y Coordinates Seperated by a Space: ")
            #takes user input and places it in a variable
            
            try:
                x, y = coordinates.split()
                x = float(x)
                y = float(y)
                #verifies if the user inputs are two numeric values
            
            except:
                print("\n")
                print("Points:", coordinateList)
                cont = False
                #creates an exception for non-numeric values that ends
                #user input and prints the coordinate list
                
            coordinateList.append((x, y))
            #adds coordinate pairs to the list
            
    del coordinateList[-1]
    #my list kept repeating the last value when I tried printing it outside
    #of the except section, so this gets rid of that repetition
    
    print("\nLocations:")
    #prints the Locations header
    
    for items in coordinateList:
    #creates the for loop
    
        location = where_is_xy(items)
        #calls the location function with tuples, then places
        #the returned value in a variable
        
        print(items, location)
        #prints the tuples and the location variable
        
    print("\nDistances:")
    #prints the Distances header

    item = 0
    #sets up the while loop

    while(item < len(coordinateList)):
    #creates a while loop that lasts the length of the list
    
        set1 = coordinateList[item]
        #puts the current tuple in the loop into a variable
        
        item += 1
        #moves the list forward
        try:
            set2 = coordinateList[item]
            #tries to put the current tuple in the loop into a variable
            
            x1 = set1[0]
            y1 = set1[1]
            x2 = set2[0]
            y2 = set2[1]
            #creates x and y variables from the tuples
            
            distance = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
            #calculates the distance formula for both coordinate paira
            
            print(set1, set2, "=", "%0.2f" % distance)
            #outputs the coordinate pairs and their distance from each
            #other
            
        except:
            print("")    
            #ends the while loop if there are no list items left, or
            #if there is no second list item

main()
#calls main function
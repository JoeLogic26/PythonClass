"""
Joseph Stallcop
CS 410P
Lab Assignment 2L

The following program reads through a series of accoustical signals and
runs a statistical analysis on them.

"""

def read_data(filename):
#creates a data reading function
    
    lst = []
    #creates a list
    
    attempt1 = True
    while attempt1 == True:
    #sets up and creates a while loop
        
        try:
            file = open(filename, "r")
            #tries to open the file
            
            for line in file:
                lst.append(float(line.strip()))
                #uses a for loop to add items from file to list in
                #stripped form
                
            if len(lst) == 0:
                file.close()
                print("Error: File is blank, please choose another")
                filename = input("Enter filename: ")
                #checks if list is empty, and if so, makes the user 
                #choose another file
            else:
                attempt1 = False
                #ends the while loop
            
        except:
            print("Error: File cannot be found. Please retype")
            filename = input("Enter filename: ")
            #makes user re-enter file if wrong name/directory is
            #given
            
        
            
    file.close()
    #closes the file
    return(lst)

def compute_variance_std(listofpts):
#creates the variance and standard deviation function
    
    sum1 = sum(listofpts)
    length = len(listofpts)
    average = sum1 / length
    #finds the average

    squareSum = 0
    #creates the sum of squared differences variable

    for answer in listofpts:
        squareSum += ((answer - average) ** 2)
        #uses a for loop to calculate the sum of squared differences

    variance = squareSum / (length - 1)
    #calculates variance
    
    std = (squareSum / (length - 1)) ** (1/2)
    #calculates standard deviation
    
    return(variance, std)
    #returns variance and standard deviation

def compute_zero(listofpts):
#creates the zero cross function

    total = 0
    count = 0
    #sets total and count variables to zero
        
    i = 1
    #sets the index variable to 1
        
    number = 0
    nextNumber = listofpts[0]
    #places the first list item in the nextNumber variable

    while i < len(listofpts):
    #creates the while loop
        
        count = listofpts[i]
        #makes the count variable current list item
        
        number = nextNumber
        nextNumber = count
        #puts the next two list items in variables
        
        if number < 0 and nextNumber >= 0:
            total += 1
        elif number >= 0 and nextNumber < 0:
            total += 1
        #checks if one number is negative whilst the other is positive
        #then keeps a running count in total variable
            
        i += 1
        #moves the index forward

        
    return(total)
    #returns the zero cross total

if __name__ == "__main__":
#creates the main function

    filename = input("Enter filename: ")
    #puts the file name into a variable
    
    list_of_numbers = read_data(filename)
    #calls the data reading function and puts results in a variable
    
    samplePoints = len(list_of_numbers)
    #puts the sample points total in a variable
    
    var, std_dev = compute_variance_std(list_of_numbers)
    #calls the variance and standard deviation function, then places
    #the results in a variable
    
    zeroCross = compute_zero(list_of_numbers)
    #calls the zero cross function and places the results in a variable
    
    print("\nNoise Statistics:")
    print("*****************")
    print("Number of Sample Points: ", samplePoints)
    print("Varience:", "%0.6f" % var)
    print("Standard Deviation:", "%0.6f" % std_dev)
    print("Zero Cross:", zeroCross)
    print("*****************")
    #outputs all calculation results
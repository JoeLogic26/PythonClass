"""
Joseph Stallcop
CS 410P
Lab Assignment 2L

The following functions assists a program in doing linear 
regression on a user inputted file of data.

"""
def read_data(fname):
    
    xLst = []
    yLst = []
    #creates x and y lists
    
    
    file = open(fname, "r")
    #opens the file
    
    for line in file:
        x, y = line.split(",")
        xLst.append(float(x))
        yLst.append(float(y))
        #uses a for loop to add items from file to list in
        #stripped form
    
    file.close()
    #closes the file
    
    return(xLst, yLst)
    #returns the two lists


def compute_m_and_b(x, y):
#creates the compute m and b function
    
    sumX = sum(x)
    lengthX = len(x)
    meanX = sumX / lengthX
    #calculates the mean of x
    
    sumY = sum(y)
    lengthY = len(y)
    meanY = sumY / lengthY
    #calculates the mean of y 

    upper = 0
    lower = 0
    #begins the for loop
    
    for i in range(0, lengthX):
    #creates the for loop for calculating the numerator and denominator
        upper += (x[i] - meanX) * (y[i] - meanY)
        lower += (x[i] - meanX) ** 2
    
    m = upper / lower
    b = meanY - (m * meanX)
    #calculates m and b

    return(m, b)
    #returns m and b


def compute_fx_residual(x, y, m, b):
#creates the compute f(x) and residual function
    
    residual = []
    fx = []
    #creates the residual and f(x) lists
    
    for i in range(0, len(x)): 
    #sets up the for list
    
        fxValue = b + m * x[i]
        fx.append(fxValue)
        #calculates f(x) and appends it to list
        
        rValue = (y[i] - fxValue)
        residual.append(rValue)
        #calcuates residual and appends it to list
        
    return(fx, residual)
    #returns f(x) and residual
        



def compute_sum_of_squared_residuals(residual):
#creates the compute sum of squared residuals fuction
    
    resSum = 0
    #sets up the for loop
    
    for i in range(0, len(residual)):
    #creates the for loop
        
        resSum += (residual[i]) ** 2
        #calculates the sum of squared residuals
    
    return(resSum)
    #returns the sum
    
    
def compute_total_sum_of_squares(y):
#creates the compute total sum of squares function
    
    sumY = sum(y)
    lengthY = len(y)
    meanY = sumY / lengthY
    #creates sum, length, and mean of y variables
    
    squSum = 0 
    #sets up the for loop
    
    for i in range(0, len(y)):
    #creates the for loop
    
        squSum += (y[i] - meanY) ** 2
        #calculates the sum of squares
    
    return(squSum)
    #returns the sum






def compute_coeff_of_determination(least_squares_r, sum_squares):
#creates the compute coefficient of determination function

    coeff = 1 - (least_squares_r / sum_squares)
    #calculates the coefficient of determination
    
    return(coeff)
    #returns the coefficient

def print_least_squares(x, y, m, b, fx, residual, least_squares_r, sum_squares, coeff_of_d):
    print("Least Squares Method")
    print("--------------------")
    print("Coefficients: m =", "%.6f" % m, "\tb =", "%.6f" % b)
    print()
    print("X\t\t\tY\t\t\tf(x)=mx+b\t\tResidual")
    #prints the headers and m and b coefficients
    
    for i in range(0, len(x)):
        print("%.6f" % x[i], "\t", "%.6f" % y[i], "\t", "%.6f" % fx[i], "\t", "%.6f" % residual[i])
        #uses a for loop to print x, y, f(x), and residual values from lists
        
    print("\nSum of Squared Residuals:\t", "%.6f" % least_squares_r)
    print("Total Sum of Squares:\t", "%.6f" % sum_squares)
    print("Coefficient of Determination:\t", "%.6f" % coeff_of_d)
    #prints sum of squared residuals, total sum of squares, and coefficient of determination
    

def compute_pearson_coefficient(x, y):
#creates the compute pearson coefficient function
    
    sumX = sum(x)
    lengthX = len(x)
    meanX = sumX / lengthX
    #calculates sum, length, and mean of x
    
    sumY = sum(y)
    lengthY = len(y)
    meanY = sumY / lengthY
    #calcuates sum, length, and mean of x
    
    sqX = 0
    sqY = 0
    covar = 0
    #sets up the for loop
    
    for i in range(0, len(x)):
    #creates the for loop
        
        covar += ((x[i] - meanX) * (y[i] - meanY)) / lengthX
        sqX += (x[i] - meanX) ** 2
        sqY += (y[i] - meanY) ** 2
        #calculates the covariance, and sum of squares
        #for x and y
        
    
    stdX = (sqX / (lengthX)) ** (1/2)
    #calculates the standard deviation for x
    
    stdY = (sqY/ (lengthY)) ** (1/2)
    #calculates the standard deviation for y
    
    pearson_r = (covar / (stdX*stdY))
    #calculates the Pearson Correlation Coefficient
    
    return(pearson_r)
    #returns the Pearson


def print_pearson(pearson_r):
    print("\n\nPearson Method")
    print("--------------")
    print("Pearson Correlation Coefficient:\t", "%.6f" % pearson_r)
    #prints the Pearson


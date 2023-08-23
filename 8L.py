"""
Joseph Stallcop
CS 410P
Lab Assignment 2L

The following program takes user input and finds both the greatest common 
divisor and the least common multiple.

"""
  
def gcd(number1, number2):
#creates the gcd function

    result = 0
    #sets an original value for result
    
    for gcdFinder in range (1, number1 + 1):
    #sets the range for the variable that loops through that range
    
        if gcdFinder <= number2:
        #sets a limit to prevent the loop from exceeding
        
            if number1 % gcdFinder == 0 and number2 % gcdFinder == 0:
                result = gcdFinder
                #verifies the variable meets the gcd requirements,
                #then places it in the result variable
                
    return(result)
    #returns the result


def lcm(number1, number2):
#creates the lcm function
    
    result = 0
    #sets the original value for the result
    
    go = True
    #sets up the while loop
    
    if number1 > number2:
      result = number1
    else:
      result = number2
    #determines which variable is greater
    
    while go == True:
    #creates the while loop
    
        if result % number1 == 0 and result % number2 == 0:
          result = result
          go = False
          #verifies the variable meets the lcm requirements,
          #then places it in the result variable and ends the
          #while loop
          
        else:
            result += 1
            #continues the while loop if the past variable isn't verified
            
    return(result)
    #returns the result

if __name__ == '__main__':
#creates the main function

    program = True
    #sets up the while loop
    
    while program == True:
    #creates the while loop
    
        try:
            number1 = int(input("\nEnter your first number: "))
            number2 = int(input("\nEnter your second number: "))
            #tries user inputs as integers
            
            if number1 > 0 and number2 > 0:
            #verifies variables are positive
            
                print("\nYou entered", number1, "and", number2)
                #outputs the user inputs
                
                gcd_result = gcd(number1, number2)
                #calls the gcd function and places it in a variable
                
                print("\nThe GCD is", gcd_result)
                #outputs the results variable
                
                lcm_result = lcm(number1, number2)
                #calls the lcd function and places it in a variable
                
                print("\nThe LCM is", lcm_result)
                #outputs the results variable
                
                program = False
                #ends the while loop
                
            else:
                print("\nError: Numbers must be greater than 0")
                #creates an error for negative values
                
        except:
            print("\nInvalid Input: Must enter 2 integers\n")
            #creates an exception for invalid inputs
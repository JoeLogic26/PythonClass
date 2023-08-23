"""
Joseph Stallcop
CS 410P
Lab Assignment 2L

The following program displays the range of Fahrenheight temperatures 
the user inputs, as well as the conversions of them to Celsius, Kelvin,
and Rankine.

"""

end = False
while end == False:
#sets up while loop to prevent invalid range    
    
    try:
        upper = int(input("Enter Start Value: "))
        lower = int(input("Enter End Value: "))
        #takes user inputs and places them in variables
        
        
        if upper < -30 or lower < -30 or upper > 130 or lower > 130:
            print("Range must be -30 - 130 degrees Fahrenheit")
            end = True
        elif upper > lower:
            print("Start value must be less than end value")
            end = True
            #prevents invalid range  
        
        else:
            f = ["Fahr"]
            c = ["Celsius"]
            k = ["Kelvin"]
            r = ["Rankine"]
            #sets up lists for each temperature form

            answer = upper
            cAnswer = 0
            kAnswer = 0
            rAnswer = 0
            #sets up starting values for while loop
            

            while answer <= lower:
            #creates a while loop that ends when the lower bound is met
        
                f.append(answer)
                #adds Fahrenheit value to list
                
                cAnswer = "%0.2f" % float(5/9 * (answer - 32))
                c.append(cAnswer)
                #converts and adds Celsius value to list
                
                kAnswer = "%0.2f" % float(5/9 * (answer - 32) + 273.15)
                k.append(kAnswer)
                #converts and adds Kelvin value to list
                
                rAnswer = "%0.2f" % float(answer + 459.67)
                r.append(rAnswer)
                #converts and adds Rankine value to list
                
                answer = answer + 1
                #increases Fahrenheit value by 1

            i = 0
            while i < len(f):
            #sets up printing while loop the length of the Fahrenheit list
            
                print("\t\t", f[i], "\t\t", c[i], "\t\t", k[i], "\t\t", r[i])
                #prints each temperature value in a table form
                
                i += 1
                #progresses through the Fahrenheit list
                
                end = True
                #ends the program after table is produced
                
    except:
        print("Error: Input must be an integer")
        end = True
        #creates an exception for invalid inputs and ends program


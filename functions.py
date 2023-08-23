"""
Joseph Stallcop
CS 410P
Lab Assignment 2L

The following are the functions of a program that takes
two user inputs of Celsius temperatures between -20 and 50,
then produces the range of Celsius temperatures between them,
their equivalent Fahrenheit temperatures, and the wind chill
and heat index temperatures for the entire range.

"""


def F(c):
#creates the Fahrenheit function

    FAHRENHEIT = (c * (9/5)) + 32
    return(FAHRENHEIT)
    #calculates and returns Fahrenheit value

def WC(f, v):
#creates the wind chill calculation function

    if f <= 50:
        WC = 35.74 + (.6215 * f) - (35.75 * v ** .16) + (.4275 * f * v ** .16)
        #sets the range and calculates wind chill
    
    else:
        WC = "X"
        #puts X's on out of range temperatures
        
    return(WC)
    #returns wind chill


def windChill(c1, c2):
#creates the wind chill function

    lst = []
    #sets up a list
    
    sublst = ["Celsius", "Fahr", "5mph", "10mph", "15mph",
              "20mph", "25mph", "30mph", "35mph", "40mph"]
    #sets up a sublist for nested list items
    
    exCold = 0
    #sets extra cold variable to 0

    for item in range(c1, c2 + 1):
    #creates the for loop to output Celsius and Fahrenheit temperatures.
        
        c = item
        #sets item as the celsius temperature
        
        f = F(c)
        #calls the Fahrenheit function for above celsius temperature
        
        if f < 0:
            exCold += 1
            #adds extreme cold days for above parameters
            
        sublst.append(float(c))
        sublst.append(float(f))
        #adds Celsius and Fahrenheit temperatures to sublist
        
        for more in range(0, 1):
        #creates a nested for loop
        
            v = 5
            wc = WC(f, v)
            #calls wind chill calculation function with above
            #velocity and current Fahrenheit temperature
            
            try:
                sublst.append(float(wc))
                #tries to append returned value as a float
                
                if wc < 0:
                    exCold += 1
                    #adds extreme cold days if parameters are met
                    
            except:
                sublst.append(wc)
                #creates an exception for non-numeric values
                
            v = 10
            wc = WC(f, v)
            try:
                sublst.append(float(wc))
                if wc < 0:
                    exCold += 1
            except:
                sublst.append(wc)
            v = 15
            wc = WC(f, v)
            try:
                sublst.append(float(wc))
                if wc < 0:
                    exCold += 1
            except:
                sublst.append(wc)
            v = 20
            wc = WC(f, v)
            try:
                sublst.append(float(wc))
                if wc < 0:
                    exCold += 1
            except:
                sublst.append(wc)
            v = 25
            wc = WC(f, v)
            try:
                sublst.append(float(wc))
                if wc < 0:
                    exCold += 1
            except:
                sublst.append(wc)
            v = 30
            wc = WC(f, v)
            try:
                sublst.append(float(wc))
                if wc < 0:
                    exCold += 1
            except:
                sublst.append(wc)
            v = 35
            wc = WC(f, v)
            try:
                sublst.append(float(wc))
                if wc < 0:
                    exCold += 1
            except:
                sublst.append(wc)
            v = 40
            wc = WC(f, v)
            try:
                sublst.append(float(wc))
                if wc < 0:
                    exCold += 1
            except:
                sublst.append(wc)
        
        lst.append(sublst)
        #appends sublist to list as nested list
        
        sublst = []
        #empties sublist for next iteration
        
    results = lst
    #creates a variable for list
    
    return(results, exCold)
    #returns list and extreme cold results


def HI(T, R):
#creates a heat index calculation function

    C1 = -42.379
    C2 = 2.04901523
    C3 = 10.14333127
    C4 = -.22475541
    C5 = -6.83783 * 10 ** -3
    C6 = -5.481717 * 10 ** -2
    C7 = 1.22874 * 10 ** -3
    C8 = 8.5282 * 10 ** -4
    C9 = -1.99 * 10 ** -6
    #sets formula constants

    if T >= 80:
        HI = C1 + (C2 * T) + (C3 * R) + (C4 * T * R) + (C5 * (T ** 2)) + (C6 * (R ** 2)) + \
            (C7 * (T ** 2) * R) + (C8 * T * (R ** 2)) + (C9 * (T ** 2) * (R ** 2))
            #calculates heat index for temperatures in the correct range
    
    else:
        HI = "X"
        #outputs X's for out of range values
        
    return(HI)
    #returns heat index calculation results


def heatIndex(c1, c2):
#creates heat index function

    lst = []
    sublst = ["Celsius", "Fahr", "40% RH", "50% RH",
              "60% RH", "70% RH", "80% RH", "90% RH", "100% RH"]
    exHeat = 0

    for item in range(c1, c2 + 1):
        c = item
        f = F(c)
        if f > 100:
            exHeat += 1
        sublst.append(float(c))
        sublst.append(float(f))
        for more in range(0, 1):
            r = 40
            hi = HI(f, r)
            try:
                sublst.append(float(hi))
                if hi > 100:
                    exHeat += 1
            except:
                sublst.append(hi)
            r = 50
            hi = HI(f, r)
            try:
                sublst.append(float(hi))
                if hi > 100:
                    exHeat += 1
            except:
                sublst.append(hi)
            r = 60
            hi = HI(f, r)
            try:
                sublst.append(float(hi))
                if hi > 100:
                    exHeat += 1
            except:
                sublst.append(hi)
            r = 70
            hi = HI(f, r)
            try:
                sublst.append(float(hi))
                if hi > 100:
                    exHeat += 1
            except:
                sublst.append(hi)
            r = 80
            hi = HI(f, r)
            try:
                sublst.append(float(hi))
                if hi > 100:
                    exHeat += 1
            except:
                sublst.append(hi)
            r = 90
            hi = HI(f, r)
            try:
                sublst.append(float(hi))
                if hi > 100:
                    exHeat += 1
            except:
                sublst.append(hi)
            r = 100
            hi = HI(f, r)
            try:
                sublst.append(float(hi))
                if hi > 100:
                    exHeat += 1
            except:
                sublst.append(hi)

        lst.append(sublst)
        sublst = []
    results = lst
    return(results, exHeat)
    #returns list and extreme heat results

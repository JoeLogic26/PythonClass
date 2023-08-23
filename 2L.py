"""
Joseph Stallcop
CS 410P
Lab Assignment 2L

This program is designed place user input into variables, output those 
variables into a table, switch the contents of those variables, and perform
calculations on both the new and original variable contents.
"""

ibA = float(input("Enter Box A Value: "))
boxA = ibA
print("Box A Value: ", boxA)
#places user input into a variable and outputs it back


ibB = float(input("\nEnter Box B Value: "))
boxB = ibB
print("Box B Value: ", boxB)

ibC = float(input("\nEnter Box C Value: "))
boxC = ibC
print("Box C Value: ", boxC)

ibD = float(input("\nEnter Box D Value: "))
boxD = ibD
print("Box D Value: ", boxD)

print("\n%21s %10s %10s %10s" % ("Box A", "Box B", "Box C", "Box D"))
print("%10s %10.2f %10.2f %10.2f %10.2f" % ("Initial:", boxA, boxB, boxC, boxD))
#produces a table for the variables in which they are formatted to 10 character
#spaces and 2 digits after the decimal point

boxA = ibB
boxB = ibC
boxC = ibD
boxD = ibA
#rearranges the orginal user inputs into different variables

print("%10s %10.2f %10.2f %10.2f %10.2f" % ("Final:", boxA, boxB, boxC, boxD))
#outputs the new variables in the table format

compute1 = float((boxC * boxD) - (boxA * boxB))
print("\nComputed Result(b): ","%.3f" % compute1)
#performs calculations on the new variables

compute2 = (ibA ** 3) + (3 * (ibA ** 2) * ibB) + (3 * ibA * (ibB ** 2)) + (ibB ** 3) 
print("\nComputed Result(c): ", "%.2f" % compute2)
#performs calculations on the original user inputs
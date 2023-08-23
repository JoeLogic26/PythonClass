"""
Joseph Stallcop
CS 410P
Lab Assignment 2L

The following program does a variety of calculations with the numbers that
the user inputs.

"""

print("Press the Enter Key to Terminate Input\n")
#giving user instruction

num =[]
done = False
while done == False:
#creates a list and sets up the while loop

    userInput = input("Enter a Number: ")
    #places user input into a variable
    
    if userInput == "":
        done = True
        print("Done!")
    #ends the while loop when the enter key is used
    
    else:
        try:
            userInput = int(userInput)
            num.append(userInput)
        #places the user inputs into a list
        
        except:
            print("Error: Must be an integer")
        #creates an exception for non-integer values
            
print("\nSize of List:", len(num))
#displays size of the list

print(num)
#displays the list

print("Sum:", sum(num))
#displays the sum of the list

print("Average:", sum(num) / len(num))
#displays the list average

print("Maximum:", max(num))
#displays the maximum value of the list

print("Minimum:", min(num))
#displays the minimum value of the list

index = int(len(num) / 2)
num2 = num[0:index]
print("First Half of List:", num2)
#divides the length of the list by 2, then uses that to index
#the list in half

answer = 0
item = 0
answer = answer + num[item]
item += 1
#puts the first number into a variable

while(item < len(num)):
#creates a while loop that lasts the length of the list
    
    answer = answer + num[item]
    item += 1
    #adds a number to the total, then moves the index
    try:
        answer = answer - num[item]
        item += 1
    #subtracts an item from the total, then moves the index
    
    except:
        answer = answer + 0
    #creates an exception if the while loop finishes before the subtraction
    #can occur
    
print("Total of Alternate Add and Subtract:", answer)
#prints the alternate add and subtract total

num.sort()
print("List Sorted in Ascending Order:", num)
#sorts list in ascending order

num.sort(reverse = True)
print("List Sorted in Descending Order:", num)
#sorts list in descending order


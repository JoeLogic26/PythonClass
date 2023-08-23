"""
Joseph Stallcop
CS 410P
Lab Assignment 2L

The following program inputs the Gettysburg address file, counts the number of total
words, counts the number of unique words, and prints a list of the greatest frequency words 
used more than 3 times.

"""

file = open('Gettysburg', "r")
#puts file into a variable

punctuation = '.,:' 
#sets a variable of punctuation

words = ""
#sets the variable words for later use

wordDict = []
wordDict2 = {}
#creates a list and a dictionary

count = 0
#prepares the for loop

for line in file:
#a for loop for lines in file

    for char in line:
    #a for loop for characters in line
    
        if char not in punctuation:
        #ignores punctuation characters
        
            char = str.capitalize(char)
            #capitalizes letters
            
            words += char
            #adds characters to words variable
            
    x = words.strip().split(" ")
    #strips words of trailing characters and splits them with space and places them in variable
    
    for items in x:
        count +=1
        #counts all items in variable
        
    wordDict.append(x)
    #appends variable to list

print("The Gettysburg Address countains", count, "words.\n")
#outputs the number of words in the original file

for lists in wordDict:
#for loop to pull the secondary list from wordDict

    for word in lists:
    #for loop for words in list
    
        if word in wordDict2:
            wordDict2[word] += 1
            #counts unique words with more than one occurence and adds to dictionary
            
        else:
            wordDict2[word] = 1
            #gives each word at least one frequency in dictionary
        
print("The Gettysburg Address countains", len(wordDict2), "different words.")
#prints the total number of unique words in dictionary

wordDict3 = wordDict2.copy()
#makes a copy of dicionary

for items in wordDict2:
    value = wordDict2[items]
    #sets values in dictionary in a variable
    
    if value < 3:
        del wordDict3[items]
        #deletes items from dictionary copy that have less than a frequency of 3

wordDict3 = sorted(wordDict3.items(), key= lambda x: x[1], reverse= True)
#adds items in dictionary, sorted by value from high to low frequency, to a list

print("")
#prints a space

print("The most common words and their frequencies are:\n")
#creates a header

for (key, value) in wordDict3:
    print(key, value)
    #outputs the list tuples
        

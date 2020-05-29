"""
Program 4
This program produces a dictionary of words with the words as a key
and the number of its occurence as a value
The keys of the dictionary are the words and the values are the
frequency of the words.
"""

__author__ = "Tejendra Khatri"
__date__ = "Oct 3,2017"

import os.path
import string

def refineList(someList):
    '''Description: This function grabs the list of words and gets rid of the punctuation
             marks at the beginning and at the end of the word.
       Pre-condition: The list should contain only strings.
    '''
    #getting all the punctuations
    punc = string.punctuation
    for ct in range(len(someList)):
        #checking if the string contains punctuations at the end
        while someList[ct][-1] in punc :
            someList[ct] = someList[ct][:-1]
        #checking if the string has punctuation at the beginning
        while someList[ct][0] in punc:
            someList[ct] = someList[ct][1:]
        someList[ct] = someList[ct].upper()
    return someList

def updateDict(aList,aDict):
    '''Description: This function updates the words and the frequency of the words in the dictionary.
       Pre-condition: It requires two parameters, firstbeing a list of strings and the second a dictionary to update.
    '''
    for item in aList:
        #adding an item to the dict if there exists none in 
        if item not in aDict:
            aDict[item] = 1
        #updateing the value if there  already exists such a word in the dictionary
        else:
            aDict[item] += 1
    return aDict

def createDict(fileObject):
    '''Description: this function creates a dictionary with the words in the file
             object as a key that maps to the frequency of the word in the file Object.
       Pre-condition: This function requires a fileObject as a parameter.
    '''
    newLine = ""
    newDict = {}
    for line in fileObject:
        newLine += line
        newLine = newLine.replace("/n"," ")
        wrdList = newLine.split()
        nonPuncList = refineList(wrdList)
    newDict = updateDict(nonPuncList,newDict)
    return newDict

def printDict(aDict):
    '''Description: This function helps to print the words and the number of
            repetition of it in a well formatted manner in a tabulated form
       Pre-condition: This functuation requires a dictionary to be printed.
    '''
    #sorting the keys of the dictionary in alphabetical order
    sortedDict = sorted(aDict)
    print("{:19s}{:3s}".format("Words","Frequency"))
    print("{:19s}{:3s}".format("-----","---------"))
    for key in sortedDict:
        print("{:19s}{:3d}".format(key,aDict[key]))

def main():
    fileName = input("Enter the name of the file:")
    if os.path.isfile(fileName):
        fileObj = open(fileName,"r")
        myDict = createDict(fileObj)
        printDict(myDict) 
        fileObj.close()
    else:
        print("There exists no such file named:",fileName)
    
if __name__ == "__main__":
    main()

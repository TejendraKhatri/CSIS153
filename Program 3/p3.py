"""
Program 3
This program deals with the addition, scalar multiplication and product of two vectors of the same size.
"""

__author__ = "Tejendra khatri"
__date__ = "9/18/2017"

import os.path

def addVectors(v1,v2):
    """
    Description: This function returns the sum of two vectors.
    Preconditions: Both the vectors v1 and v2 must have equal number of items and should be lists.
    """
    newList = []
    for n in range(len(v1)):
        v1[n]= int(v1[n]) ; v2[n] = int(v2[n])
        temp = v1[n] + v2[n]
        newList.append(temp)
    return newList

def scalarMult(s,v):
    """
    Description:This function returns a vector multiplied by a scalar number.
    """
    tmpList = []
    for n in range(len(v)):
        v[n] = int(v[n])
        a = int(s) * v[n]
        tmpList.append(a)
    return tmpList

def dotProduct(v1,v2):
    """
    Description:This function returns the sum of the product of corresponding elements of the vectors.
    Preconditions: Both the vectors must have equal number of elements.
    """
    newList = []
    for n in range(len(v1)):
        v1[n]= int(v1[n]) ; v2[n] = int(v2[n])
        temp = v1[n] * v2[n]
        newList.append(temp)
    return sum(newList)

def main():
    #prompting the user for the name of the file
    fName= input("Please enter the name of the file:")
    #checking if the file exists
    if os.path.isfile(fName):
        #opening the file
        fObj = open(fName,"r")
        for line in fObj:
            line = line.rstrip('\n')
            newList = line.split()
            
            if newList[0] == "S":
                scalrNum = newList[1]
                vector = newList[3:]
                result = scalarMult(scalrNum,vector)
                print("Scalar multiplication:",scalrNum, "*",vector,"=", result)
            elif newList[0] == "A" or newList[0] == "D":
                #checking how many items are in individual vectors
                numItemVec = int(newList[1])
                #assigning the values from the file in respective vectors
                v1 = newList[2:(numItemVec + 2)]                
                v2 =newList[(numItemVec +2):]
                
                if newList[0] == "A":
                    result = addVectors(v1,v2)
                    print("Vector Addition:",v1,"+",v2,"=",result)
                elif newList[0] == "D":
                    result = dotProduct(v1,v2)
                    print("Vector multiplication:",v1,"*",v2,"=",result)
                
        #closing the file object after using it
        fObj.close()

    else:
        print("There exists no such file named",fName,"\n","Please try again!")


if __name__ == "__main__":
    main()









"""
Program 2
This program differentiates a valid phone number and an invalid one.
"""

__author__ = "Tejendra Khatri"
__date__ = "Sep 6, 2017"



def isValidPhone(phoneNum):
    """
        Description: This function checks whether a given number is valid or not.
        precondition: The parameter requires to be a string.
    """
    
    #checking the length of the number
    if len(phoneNum) == 13 or len(phoneNum) == 12 :
        #checking for the number of type (###)###-####
        if phoneNum[0] == "(" and phoneNum[4] == ")" and phoneNum[8]=="-":
            areaCode = phoneNum[1:4]
            prefixCode = phoneNum[5:8]
            endDigit = phoneNum[9:]
            #creating the phone number in ########## format
            phoneNumber = areaCode + prefixCode + endDigit
            #checking if the string contains only digits
            if phoneNumber.isdigit() and len(phoneNumber)== 10:
                result = True
            else:
                result = False
                
        #checking for the number of the type ###-###-####   
        elif phoneNum[3] == "-" and phoneNum[7] == "-":
            areaCode = phoneNum[0:3]
            prefixCode = phoneNum[4:7]
            endDigit = phoneNum[8:]
            phoneNumber = areaCode + prefixCode + endDigit
            
            if phoneNumber.isdigit() and len(phoneNumber) == 10:
                result = True
            else:
                result = False
        else:
            result = False
            
    else:
        result= False

    return result


def main():
    import os.path
    #prompting the user to enter the name of the text file
    fileName = input("Enter the name of the text file containing phone numbers:")
    #checking if the file exists
    if os.path.isfile(fileName):
        fileObject = open(fileName,"r")
        phnList = fileObject.readlines()
        #iterating over the phone numbers in the text file
        for num in phnList:
            num = num.rstrip("\n")
            if isValidPhone(num):
                print(num,"is a valid phone number.")
            else:
                print(num,"is an invalid phone number.")
        
        fileObject.close()
    else:
        print("There exists no such file with the name:",fileName)



if __name__ == "__main__":
    main()


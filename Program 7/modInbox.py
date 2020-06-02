"""
This class creates a type for Inboxes.
"""
__author__ = "Tejendra Khatri"
__date__= "11/06/2017"

def isValidPhone(phoneNum):
    """
        Description: This function checks whether a given number is valid or not.
        precondition: The parameter requires to be a string.
        Postcondition: Returns a boolean value false if invalid phone number or else otherwise
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

def isValidDay(dayName):
    """Description: checks the validity of the name of the day
       precondition: parameter must be a string
       postcondition: returns a boolean value
    """
    dayList = ["sun","mon","tues","wed","thurs","fri","sat"]
    if dayName.lower() in dayList:
        return True
    else:
        return False

    
class Inbox:
    def __init__(self):
        """Description: creates an object of type Inbox
           Pre-conditions: None
           Postconditions: None
        """
        self.__msgList = []

    def __str__(self):
        """Description: returns the object in a string format 
           Pre-conditions: None
           Postconditions: None
        """
        msg = ""
        for subList in self.__msgList:
           newMsg = "{0:14s}{1:30s}{2:5s}{3:8s}\n".\
                    format(subList[0],subList[1],subList[2],str(subList[3]))
           msg += newMsg
        if self.__msgList != []:
            return msg
        else:
            return "Inbox is empty!"

    def addNewArrival(self,tmpPhnNum,tmpMsg,tmpArrival):
        """Description: adds a new message to the object created
           Pre-conditions: takes three parameters phoneNumber, message and \
           arrival day in string format
           Postconditions: adds a list to the inbox with an additional of \
                           boolean value referring to as the message has been read or not 
        """
        charList = list(tmpMsg)
        charLimit = 140
        aList = []
        for ct in range(0,len(tmpMsg),charLimit):
            aList.append("".join(charList[:charLimit]))
            del charList[:charLimit]
        for eachMsg in aList:
            self.__msgList.append([tmpPhnNum,eachMsg,tmpArrival,False])
            
               
    def countMessages(self):
        """Description: counts the total number of messages in the inbox
           Pre-conditions: None
           Postconditions: returns an integer
        """
        return len(self.__msgList)

    def clearInbox(self):
        """Description: clears the contents of the inbox object
           Pre-conditions: None
           Postconditions: None
        """
        self.__msgList = []

    def getUnread(self):
        """Description: returns the messages in the inbox that have not been read
           Pre-conditions: None
           Postconditions: returns a string if all messages are read else \
           returns a list of unread messages
        """
        unreadList = []
        for subList in self.__msgList:
            if subList[3] == False:  
                unreadList.append(subList)
                subList[3] = True
        if len(unreadList) != 0:
            return unreadList
        else:
            return "No unread messages!"

    def getMsgsFromPhone(self,phoneNum):
        """Description: returns all the messages from a specific phone number
           Pre-conditions: takes a phone number in string format 
           Postconditions: returns 
        """
        phnMsgList = []
        for subList in self.__msgList:
            if subList[0] == phoneNum:
                subList[3] = True
                phnMsgList.append(subList)
        return phnMsgList
    


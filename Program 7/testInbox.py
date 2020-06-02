from modInbox import *


myInbox = Inbox()
print("Creating an inbox from my messages",end = ' ');print(myInbox)

print("Adding a new message to the inbox")
wish = input("Do you want to add a new message to the inbox?\n\
Type any key to continue or NO to exit")
while wish.upper() != "NO":
    phnNum = input("Please enter the phone number:")
    while not isValidPhone(phnNum):
        phnNum = input("INVALID CHOICE!!\nPlease enter a valid phone number:")
    inMsg = input("Enter the text message:")
    daySent = input("Enter the day the message was received in abbreviated form \n \
    eg. 'Mon','Tues','Wed','Thurs','Fri','Sat','Sun':")
    while not isValidDay(daySent):
        print("ERROR!!!")
        daySent = input("Enter the day the message was received in abbreviated form \n \
    eg. 'Mon','Tues','Wed','Thurs','Fri','Sat','Sun':")
    myInbox.addNewArrival(phnNum,inMsg,daySent)
    wish = input("Do you want to add a new message to the inbox?\n\
Type any key to continue or NO to exit")

print("Inbox after arrival of Messages");print(myInbox)

print("Checking the total number of messages in the inbox")
numMsg = myInbox.countMessages()
print("Total number of messages in the inbox:",numMsg)

print("Checking the unread messages in the inbox.")
print("Unread Messages:");print(myInbox.getUnread())

print("Checking the messages from a specific phone number")
msgFind = input("Enter the phone number to look at the messages associated with the number:")
while not isValidPhone(msgFind):
    msgFind = input("Enter the phone number to look at the messages associated with the number:")
print("Messages from the phone number",msgFind,"are:");print(myInbox.getMsgsFromPhone(msgFind))

print("Clearing the inbox")
myInbox.clearInbox()
print("Inbox after clearing it:",myInbox)








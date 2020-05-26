"""
PROGRAM 1
This programs deals with the deposit and withdrawal of amount from a bank account,\
   using the data from a text file.
"""

__author__ = "Tejendra Khatri"
__date__ = "Aug 28, 2017"

import os.path

def handleDeposit(depAmt, balance):
    '''This function handles the deposits of amount into the bank balance and returns the new balance after the deposit.
        Preconditions: Both the parameters are required to be floats.'''

    updatedBal = depAmt + balance
    return updatedBal

def handleWithdrawal(withAmt, balance):
    '''This function deals with the withdrawals and returns the new balance after withdrawal
                  or a string if the withdrawal amount exceeds the current balance.
       Preconditions: Both the parameters withdrawal amount and balance need to be floats.'''
    #checking to make sure that the withdrawal amount is less than the balance to avoid overdraft
    if withAmt<= balance:
        updatedBal = balance - withAmt
    else:
        updatedBal = str()
    return updatedBal

def updateBalance(amt, balance, transactionType):
    '''This function deals with the type of transaction i.e either deposit or withdrawal
            and returns the updated bank balance accordingly.
       Preconditions: The parameters 'amt', 'balance' are required to be floats whereas the
                 'transactionType' is required to be a string; 'D' or'W' to be specific.'''
    
    if transactionType == "D":
        updatedBal = handleDeposit(amt,balance)
    elif transactionType == "W":
        result = handleWithdrawal(amt,balance)
        #checking that the withdrawal function has returned a float
        if (type(result) == float):
            updatedBal = result
        else:
            print("You can not withdraw more than your current balance-:","$"+str(balance))
            updatedBal=balance
    return updatedBal
    
def main():
    #initializing the counters for total deposit, total withdrawal and current balance
    currentBal = 0
    totalDeposits = 0
    totalWithdraw = 0
    fileName = input("Enter the name of the file:")
    #Checking to see if the file exists
    if os.path.isfile(fileName):
        #opening the file
        myFileObject = open(fileName, "r")
        for tmpLine in myFileObject:
            tmpList = tmpLine.split()

            newBalance = updateBalance(float(tmpList[1]),currentBal,tmpList[0])
            #updating the values of total deposit and total withdrawals 
            if tmpList[0]=="D":
                totalDeposits += float(tmpList[1])
            elif tmpList[0] == "W":   
                if float(tmpList[1]) <= currentBal:
                    totalWithdraw += float(tmpList[1])
                   
            currentBal = newBalance
            
        print("Total Deposits- ","$"+str(totalDeposits))
        print("Total Withdraw- ","$"+str(totalWithdraw))
        print("Your Balance- ","$"+str(currentBal))
        #closing the text file
        myFileObject.close()
    else:
        print("There exist no file with the name,",fileName)


if __name__ == "__main__":
    main()
    



 



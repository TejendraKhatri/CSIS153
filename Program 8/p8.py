"""
This program contains two functions calcDiff, that calculates\
the difference between two dates and calcLateFee, that calculates the \
 late fee based on current date and due date.
"""

__author__ = "Tejendra Khatri"
__date__ = "11/15/2017"

from datetime import *
from calendar import *

def calcDiff(date1,date2):
    """
    Description:This function calculates the difference of two dates.
    Precondition: It requires two dates of type date.
    Postconditions:It returns a list containing the difference in years months and days.
    """
    if date1>=date2:
        diffInDates = date1 - date2
    else:
        diffInDates = date2 - date1
    diffInYears = diffInDates.days // 365
    residualMnth = (diffInDates.days % 365) // 30
    residualDays = diffInDates.days - diffInYears * 365 -residualMnth *30
    return [diffInYears,residualMnth,residualDays]

def calcLateFee(dueDate,curDate,dailyFee):
    """
    Description: This function calculates the late fee.
    Precondition: It takes two date parameters of type date and \
                   a float representing the daily late fee.
    Postcondition: It returns a float.
    """
    if curDate > dueDate:
        delayTime = calcDiff(curDate,dueDate)
        delayTimeDays = delayTime[0] * 365 + delayTime[1] * 30 + delayTime[2]
    else:
        delayTimeDays = 0
    lateFee = delayTimeDays * dailyFee
    return lateFee

def getValidYear(year):
    """
    Description:This function checks the validity of the year
    Precondition:It takes a string as a parameter and considers a year from 1000 to 9999(included) as valid.
    PostCondition:It returns a boolean value.
    """
    if year.isdigit() and 999<int(year)<10000:
        return True
    else:
        return False

def getValidMonth(mnth):
    """
    Description:This function checks the validity of a month
    Precondition:It takes a string as a parameter.
    PostCondition:It returns a boolean value.
    """
    if mnth.isdigit() and 0<int(mnth)<13:
        return True
    else:
        return False

def getValidDay(year,month,day):
    """
    Description:This function checks the validity of a day in a month of a specific year.
    Precondition:It takes a year a month and a day as a parameter of str type
    PostCondition:It returns a boolean value.
    """
    #checking the max num of days in a particular month of a particular year
    maxDays = monthrange(int(year),int(month))[1]
    if day.isdigit() and 0<int(day)<(maxDays +1):
        return True
    else:
        print("The month has only",maxDays,"days.")
        return False
    
def main():
    year = input("Enter the year in #### format (eg. 2070) or END to stop:")
    while year.lower() != "end":
        if getValidYear(year):
            month = input("Enter the month in digit (eg. 1 for Jan,2 for Feb etc.:")
            while not getValidMonth(month):
                print("Invalid input!")
                month = input("Enter the month in digit (eg. 1 for Jan,2 for Feb etc.:")
            day = input("Enter the day:")
            while not getValidDay(year,month,day):
                print("Invalid input!")
                day = input("Enter the day:")
            userDate = date(int(year),int(month),int(day)) 
            todayDate  = date.today()
            diffInDates = calcDiff(todayDate,userDate)
            print("The difference in dates between",todayDate,"and",userDate,\
                  "is", diffInDates[0],"years",diffInDates[1],"months and", diffInDates[2],"days.")
            lateFeeRate = input("Enter the amount of late fee per day:")
            while lateFeeRate.isalpha() or not isinstance(float(lateFeeRate),float) or float(lateFeeRate)<0:
                print("Invalid Input")
                lateFeeRate = input("Enter the amount of late fee per day:")
            lateFee = calcLateFee(userDate,todayDate,float(lateFeeRate))
            print("{0:25s}  ${1:<15.2f}".format("The total amount of late fees due is", lateFee))
            
        else:
            print("Invalid Input!")
        year = input("Enter the year in #### format (eg. 2070) or END to stop:")
    

    print("The program has terminated.")
    
        


if __name__ == "__main__":
    main()

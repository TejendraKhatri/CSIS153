"""
Program 5
This program helps to create a menu using dictionaries that maps  and to add or remove employee, /
calculate the average salary of the employees, print the info for a particular employee or for all employees.
"""

__author__ = "Tejendra Khatri"
__date__ = "Oct 12 2017"

def createMenu(itemList):
    '''Description: This function creates a menu of items contained in a list.
       Preconditions: A list must be passed as a parameter.
    '''
    ct =1
    theMenu =""
    for wd in itemList:
        theMenu += str(ct) +'.' +wd + '\n'
        ct  += 1
    return theMenu


def getValidChoice(menuString,highestMenuNum):
    '''Description: This function ensures that the user enters a valid choice from the menu and returns the choice.
       Preconditions: It requires a menu string and the highest value that the user can enter.
    '''
    print(menuString)
    choice = input("Please choose a number from the list above:")
    #checking that the user only types numbers within the range
    while not choice.isdigit() or int(choice) > highestMenuNum:
        print("\nERROR!--Invalid Choice\n")
        print(menuString,"\n")
        choice = input("Please enter the NUMBER of your choice from the list:")
    return int(choice)

def isValidSSN(tempSSN):
    '''Description: This function checks whether the SSN is valid or not and; returns True if valid and vice versa.
       Preconditions: This function takes a string as a parameter.
    '''
    if len(tempSSN) == 11 and tempSSN[0:3].isdigit() and tempSSN[4:6].isdigit() \
                      and tempSSN[7:].isdigit() and tempSSN[3] == "-" and tempSSN[6] == "-":
        return True
    else:
        return False

def addEmployee(dictionary):
    '''Description:This function adds an employee to the dictionary making sure\
                          that there are no two employees with the same SSN.
       Preconditions: This function takes a dictionary that needs to be updated as a parameter.
    '''
    name = input("\nEnter the name of the new employee:")
    salary = input("\nEnter the salary of the employee without '$' (eg: 45000):")
    while not salary.isdigit():
        salary = (input("\nERROR! Please enter the salary of the employee without '$' (eg: 45000):"))
    SSN = input("\nEnter the SSN of the employee in ###-##-#### form:")
    #ensuring that the SSN is valid and does not exist in the dictionary already
    while not isValidSSN(SSN) or SSN in dictionary:
        SSN = input("\nThe SSN you entered is either incorrect or a duplicate.\
                          \nPlease enter a different valid SSN:")
    #add the employee to the roster
    dictionary[SSN] = [name,salary]
           
        
def printReport(dictionary):
    '''Description:This function prints the SSN ,name and salary of the employees contained  in the \
                    dictionary in a well formatted table.
       Precondition:It takes the dictionary as a parameter.
    '''
    tmp = "{0:15s}{1:20s}\t{2:13s}".format("SSN","Name","Salary")
    print("\n",tmp)
    print("_"*67)
    for SSN in dictionary:
        tmpStr = "{0:15s}{1:20s}\t${2:<13.1f}".format(SSN,dictionary[SSN][0].upper(),float(dictionary[SSN][1]))
        print(tmpStr)

def printInfo(dictionary):
    '''Description:This function prints the SSN ,name and salary of a specific employee contained  in the \
                    dictionary .
       Precondition:It takes the dictionary as a parameter.
    '''
    nameToFind = input("Enter the name of the employee:")
    found = False
    for SSN in dictionary:
        if dictionary[SSN][0].upper() == nameToFind.upper():
            found = True
            print("\n{0:10s}{1:25s}\n{2:10s}{3:15s}\n{4:10s}${5:10s}\n"\
                  .format("Name:",nameToFind.upper(),"SSN:",SSN,"Salary:",dictionary[SSN][1]))
    if not found:
        print("\nThere is no employee with such name in the roster!")

def avgSal(dictionary):
    '''Description:This function calculates and returns the average of the salaries of the employees \
                       and reurns 0 if dictionary contains no employees.
       Precondition:It takes the dictionary as a parameter.
    '''
    if len(dictionary) != 0:
        salList = []
        for SSN in dictionary:
            salList.append(int(dictionary[SSN][1]))
        averageSal = sum(salList)/len(salList)
        return averageSal
    else:
        print("\nThere are no employees to calculate the mean of their salaries.")
        return 0

def delEmployee(dictionary):
    '''Description:This function deletes the information of a particular employee that \
                      the user wants from the dictionary.
       Precondition:It takes the dictionary as a parameter.
    '''
    if len(dictionary) != 0:
        ssnList = []
        for SSN in dictionary:
            ssnList.append(SSN)
        ssnMenu = createMenu(ssnList).rstrip('\n')
        ssnNewList = ssnMenu.split("\n")
        choice = getValidChoice(ssnMenu,len(ssnList))
        for SSN in ssnNewList:
            if str(choice) == SSN[0]:
                employeeSSN = SSN[2:]
                del dictionary[employeeSSN]
                print("\nSuccessfully Deleted!")
    else:
        print("\nThere are no any employees in the roster to delete.")


def main():
    menu = ["Add Employee","Print Report","Print Info for Individual Employee",
            "Calculate Average Salary of all Employees","Delete Employee","Quit"]
    #creating an empty dictionary
    empRoster = {}
    menuOptionList = createMenu(menu)
    task = getValidChoice(menuOptionList,len(menu))
    while task != len(menu):
        if task == 1:
            addEmployee(empRoster)
        elif task == 2:
            printReport(empRoster)
        elif task == 3:
            printInfo(empRoster)
        elif task == 4:
            meanSal = avgSal(empRoster)
            if meanSal != 0:
                print("The average salary of all employees is ${0:<10.1f}".format(meanSal))
        elif task == 5:
            delEmployee(empRoster)
        print('\n')
        task = getValidChoice(menuOptionList,len(menu))
    print("\nThank you for using my program!")


if __name__ == "__main__":
    main()

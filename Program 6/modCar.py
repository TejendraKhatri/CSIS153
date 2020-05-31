'''
This program consists of a class called Car which has three attributes 
brand name, make year and price of the car.
'''

__author__ = "Tejendra Khatri"
__date__ = "Oct 2, 2017"

class Car:
    def __init__(self, tmpBrandName, tmpMakeYear, tmpPrice): #constructor
        self.__brand = tmpBrandName
        self.__makeYear = tmpMakeYear
        self.__price = tmpPrice

    def __str__(self):
        return "Brand:"+self.__brand + "\n" + "Make Year:"+str(self.__makeYear) +\
               "\n" + "Price:"+str(self.__price)

    def getBrand(self): #getter for brand name
        return self.__brand

    def setBrand(self,newBrandName): #setter for brand name
        self.__brand = newBrandName

    def getMakeYear(self): #getter for make year
        return self.__makeYear

    def setMakeYear(self,newMakeYear):#setter for make year
        self.__makeYear = newMakeYear

    def getPrice(self):  #getter for price
        return self.__price

    def setPrice(self, newPrice):#setter for price
        self.__price = newPrice

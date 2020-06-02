"""
This modules consists of classes relates to vehicles.
"""

__author__ = "Tejendra Khatri"
__date__ = "11/20/2017"


from datetime import *
class Vehicle:
    __numVehicles = 0
    def __init__(self,tmpVIN,tmpType,tmpColor,yrMan):
        """Description: creates an object of type Vehicle
           Pre-condition:takes 4 parameters
           Post-condition: nOne
        """
        self.__VIN = tmpVIN
        self.__type = tmpType
        self.__color = tmpColor
        self.__yrMan = yrMan
        Vehicle.__numVehicles += 1
        self.__vehicleAge = (date.today()).year - self.__yrMan

    def __str__(self):
        """Description: returns the object as a string
           Pre-condition:None
           Post-condition: nOne
        """
        return "\nVIN:" + str(self.__VIN) +"\nType:" + self.__type +\
               "\nColor:" + self.__color + "\nYear Manufactured:" +\
               str(self.__yrMan) + "\nVehicle Age:" + str(self.__vehicleAge)

    def getNumVehicles():
        """Description: returns the number of vehicles created
           Pre-condition:None
           Post-condition: returns an integer
        """
        return Vehicle.__numVehicles

    def getVin(self):
        """Description: returns the VIN of the vehicle
           Pre-condition:None
           Post-condition: returns an integer
        """
        return self.__VIN

    def getVehicleType(self):
        """Description: returns the type of the vehicle
           Pre-condition:NONE
           Post-condition:returns a string 
        """
        return self.__type

    def getYearManufactured(self):
        """Description: returns the year the vehicle was created
           Pre-condition:none
           Post-condition: returns an integer
        """
        return self.__yrMan

    def getColor(self):
        """Description: returns the color of the vehicle
           Pre-condition:None
           Post-condition: returns a string
        """
        return self.__color

    def calcVehicleAge(self):
        """Description: calculates the age of the vehicle
           Pre-condition:NONE
           Post-condition:returns an integer
        """
        return self.__vehicleAge




class Car(Vehicle):
    __numHondas = 0
    def __init__(self,tmpVIN,tmpCarType,tmpColor,tmpMakeYear):
        """Description: creates an object of type car
           Pre-condition:takes four parameters VIN as integer, carType as String,\
                        color as string and make as integer
           Post-condition:NONE
        """
        if tmpCarType.upper() == "HONDA":
            Car.__numHondas += 1
        self.__carType = tmpCarType
        Vehicle.__init__(self,tmpVIN,"Car",tmpColor,tmpMakeYear)

    def __str__(self):
        """Description: returns the object in string format
           Pre-condition:NONE
           Post-condition:returns a string
        """
        return Vehicle.__str__(self) +"\nCar Type:" +\
               self.__carType

    def getCarType(self):
        """Description: gets the type of the car
           Pre-condition:NONE
           Post-condition:returns a string
        """
        return self.__carType

    def getNumHondas():
        """Description: gets the number of Honda card
           Pre-condition:NONE
           Post-condition:returns an integer
        """
        return Car.__numHondas
        
        

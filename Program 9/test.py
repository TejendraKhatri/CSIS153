from modVehicle import *

print("Creating car objects".upper())
arjunCar = Car(1234,"Honda","Black",2000)
sushilCar = Car(2345,"Suzuki","Green",2015)
rajuCar = Car(1000,"HONDA","Black",1995)
print("Arjun Car:",arjunCar);print("\nSushil Car:",sushilCar)
print("\nRaju Car:",rajuCar)
#
print("="*60)
print("CHECKING THE TOTAL NUMBER OF VEHICLES")
print("Total vehicles created:",Car.getNumVehicles())
#
print("="*60)
print("CHECKING THE GETTERS")
print("\nCHECKING THE getVin GETTER:")
rajuVin = rajuCar.getVin()
print("VIN of Raju's car:",rajuVin)
##
print("\nCHECKING THE getVehicleType GETTER:")
arjunCarType =arjunCar.getVehicleType()
print("Vehicle type of Arjun:",arjunCarType)
##
print("\nCHECKING THE getYearManufactured GETTER:")
rajuCarManuf = rajuCar.getYearManufactured()
print("Year Manufactured of Raju's car:",rajuCarManuf)
##
print("\nCHECKING THE getColor GETTER:")
sushilCarColor = sushilCar.getColor()
print("Color of Sushil's car:",sushilCarColor)
##
print("\nCHECKING THE calcVehicleAge:")
print("Age of arjun's car:",arjunCar.calcVehicleAge())
##
print("\nCHECKING THE getNumHondas:")
print("Total number of Hondas:",Car.getNumHondas())













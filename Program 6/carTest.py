'''
This program tests the class Car and the getters and the setters contained within.
'''
__author__ = "Tejendra Khatri"
__date__ = "Oct 1, 2017"

from modCar import *

car1 = Car("Hyundai" , 2010, 45000)
car2 = Car("Chevrolet", 2017, 89000)
print("Details of car1:");print(car1,"\n")
print("Details of car2:");print(car2,"\n")
print("Testing getters for car1:")
model = car1.getBrand()  
print("Retrieved Model Name:",model)
madeYear = car1.getMakeYear()
print("Retrieved Make Year:",madeYear)
price = car1.getPrice()
print("Retrieved Price:", price)
print("\nTesting setters for car2:")
car2.setBrand("Toyota") #changing the brand name of car 2
print("Changed the brand name from Chevrolet to :", car2.getBrand())
car2.setMakeYear(1995) #changing the make year of car 2
print("Changed the make year from 2017 to:", car2.getMakeYear())
car2.setPrice(25000) #changing the price of car 2
print("Changed the price from 89000 to:",car2.getPrice())
print("\nUpdated details of car2:");print(car2)



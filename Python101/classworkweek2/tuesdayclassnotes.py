##### CLASS

# student1 = "Tarek"
# student2 = "Chris"
# student3 = "Michael"

# def Students():
#     print(f"{student1} {student2} {student3}")

# Students()

# student1 = "Glen"

# Students()

#####3 GLOBAL FUNCTION

# class Students:

#     def PrintStudents():
#         print("Tarek Chris Michael")

# Students.PrintStudents()

#### CLASS CAN HOLD FUNCTIONS

# class Students:

#     def students(self):
#         print("Tarek Chris Michael")

# Michael = Students()
# Michael.students()

# Chris = Students()
# Chris.students()

#### __init__ = global class variables

# class MyClass(object):
#     def __init__(self):
#         print("hello world")
#         self.first_name = "Kevin"
#         self.last_name = "Evangelista"

#     def printName(self):
#         print(f"{self.first_name} {self.last_name}")

# dc = MyClass()
# dc.printName()

##### STILL DONT GET IT

# class MyClass(object):
#     def __init__(self, first_name, last_name):
#         print("hello world")
#         self.first_name = first_name
#         self.last_name = last_name

#     def printName(self):
#         print(f"{self.first_name} {self.last_name}")

# dc = MyClass("Chris", "Humphrey")
# dc.printName()

# dc_houston = MyClass("Mohammad", "Azam")
# dc_houston.printName()

#####

# def Person(name, count):

#     print(f"my name is {name} {count}")
#     count = count + 1
#     return count

# count = Person("Lisa", 0)
# count = Person("Lisa", 1)

# print(count)

#####

# class Person(object):
#     def __int__(self, name):
#         self.name = name
#         self.count = 0
#         self.whoAmI = whoAmI
#         # print(f"hello {self.name}")

#     def change_name(self, new_name):
#         self.name = new_name
#         self.count = self.count + 1
#         print(f"who am i: {self.whoAmI} name: {self.name} count:{self.count}")

# student = Person("Kevin", "student")
# atlanta_student = Person("Michael", "atlanta_student")

# student.change_name("Matt")
# student.change_name("Andrew")
# student.change_name("Sabrina")
# atlanta_student.change_name("Jake")

##### MY TRY AT MAKING CLASS OF PHONE TYPE

# class Phone(object):
#     def __init__ (self, phone_name):
#         self.phone_name = phone_name
#         print(f"what kind of phone do you have? {self.phone_name}")

#     def change_phone(self, new_phone):
#         self.phone_name = new_phone
#         print(f"what new phone do you have?: {self.phone_name}")

# cell = Phone("apple")

##### MAKING CLASS OF PHONE TYPE (slowly understanding)

# class Phone(object):
#     def __init__ (self, phone_type):
#         self.phone_type = phone_type
#         self.status = "off"
#         print(f"my phone is a {self.phone_type}")

#     def print_phone(self):
#         print(self.phone_type)

#     def on(self):
#         print('You have turned your phone on')
#         self.status = "on"

#     def off(self):
#         print('Your phone is turned off')
#         self.status = "off"

#     def get_status(self):
#         print(f"your {self.phone_type} is currently: {self.status}")


# android = Phone("Android")
# iPhone = Phone("iPhone")
# blackberry = Phone("Blackberry")


# android.get_status()
# android.on()
# android.get_status()

# iPhone.get_status()
# blackberry.get_status()

########

# class Car:
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.doorStatus = "closed"
#         print(f"make: {self.make}, model: {self.model}, color: {self.color}")

#     def ChangeColor(self, newColor):
#         self.color = newColor

#     def openDoor(self):
#         self.doorStatus = "open"

#     def displayColor(self):
#         print(f"The color of your {self.make} is {self.color}")

#     def displayInfo(self):
#         print(f"make: {self.make}, model: {self.model}, color: {self.color}")

# toyota = Car("Toyota" , "Prius" , "Green")

# honda = Car("Honda" , "Civic" , "White")

# jeep = Car("Jeep" , "Wrangler" , "White")

# f150 = Car("Ford" , "F150" , "Marble")

# f150.ChangeColor("Midnight Red")
# f150.displayColor()

# toyota.displayInfo()
# honda.displayInfo()
# f150.displayInfo()
# jeep.displayInfo()

# fleet = [toyota, honda, jeep, f150]

# for carObject in fleet:
#     print(carObject.displayInfo())

######## HOW TO ADD CONSTANTS (did not understand)

# class Car:
#     pi = 0
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.doorStatus = "closed"
#         print(f"make: {self.make}, model: {self.model}, color: {self.color}")
#         self.myList = []

#     def ChangeColor(self, newColor):
#         self.color = newColor

#     def openDoor(self):
#         self.doorStatus = "open"

#     def displayColor(self):
#         print(f"The color of your {self.make} is {self.color}")

#     def displayInfo(self):
#         print(f"make: {self.make}, model: {self.model}, color: {self.color}")

#     def cir(self, length):
#         return 2 * car.pi * length

# print(Car.pi)
# Car.pi = 4

# toyota = Car("Toyota" , "Prius" , "Green")

# honda = Car("Honda" , "Civic" , "White")

# jeep = Car("Jeep" , "Wrangler" , "White")

# f150 = Car("Ford" , "F150" , "Marble")

# print(toyota.pi)

# f150.ChangeColor("Midnight Red")
# f150.displayColor()

# toyota.displayInfo()
# honda.displayInfo()
# f150.displayInfo()
# jeep.displayInfo()

# fleet = [toyota, honda, jeep, f150]

# for carObject in fleet:
#     print(carObject.displayInfo())


########

##### self.email = instance variable
##### person.email = instance variable

# import datetime # we will use this for date objects
# class Person:
#     def __init__(self, name, surname, birthdate, address, telephone, email):
#         self.name = name
#         self.surname = surname
#         self.birthdate = birthdate
#         self.address = address
#         self.telephone = telephone
#         self.email = email
#     def age(self):
#         today = datetime.date.today()

#         age = today.year - self.birthdate.year
    
#         if today < datetime.date(today.year, self.birthdate.month, 
#         self.birthdate.day):
#             age -= 1
#         return age

# person = Person(
#     "Jane",
#     "Doe",
#     datetime.date(1992, 3, 12), # year, month, day
#     "No. 12 Short Street, Greenville",
#     "555 456 0987",
#     "jane.doe@example.com"
# )

# print(person.name)
# print(person.email)
# print(person.age())

####### ??????????????????????

# class Person:
#     def __init__ (self, name):
#         self.name = name
#         self.count = 0
    
#     def greet(self):
#         self._greet()
#         def _greet (self):
#             self.count += 1

#     if self.count > 1:
#         print("Stop being so nice")
#         self.__reset_count()
#     else:
#         print("Hello", self.name)
#     def __reset_count(self):
#         self.count = 0

# person = Person("Kevin")

# person.greet()

########### INHERITANCE

# class Animal:
#     def __init__ (self, name):
#         self.name = name

# class Dog (Animal):
#     def woof (self):
#         print("Woof")

# puppy = Dog("Pickle")
# print(puppy.name)

# puppy2 = Dog("John Luke")
# print(puppy2.name)

# class Cat (Animal):
#     def meow (self):
#         print("Meow")

# cat1 = Cat("Misty")
# cat2 = Cat("Bubbles")
# print(cat1.name)
# print(cat2.name)

########## INHERITANCE WITH CARDS

# class Car:
#     pi = 0
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.doorStatus = "closed"
#         print(f"make: {self.make}, model: {self.model}, color: {self.color}")
#         self.myList = []

#     def ChangeColor(self, newColor):
#         self.color = newColor

#     def openDoor(self):
#         self.doorStatus = "open"

#     def displayColor(self):
#         print(f"The color of your {self.make} is {self.color}")

#     def displayInfo(self):
#         print(f"make: {self.make}, model: {self.model}, color: {self.color}")

#     def cir(self, length):
#         return 2 * car.pi * length

# class ElectricCar(Car):

#     def printCarType(self):
#         print("I am an electric car")

# ec = ElectricCar("tesla", "s", "red")

# ec.printCarType()

######## OVERRIDE FUNCTION (INCOMPLETE)

# class Car:
#     pi = 0
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.doorStatus = "closed"
#         print(f"make: {self.make}, model: {self.model}, color: {self.color}")
#         self.myList = []

#     def ChangeColor(self, newColor):
#         self.color = newColor

#     def openDoor(self):
#         self.doorStatus = "open"

#     def displayColor(self):
#         print(f"The color of your {self.make} is {self.color}")

#     def displayInfo(self):
#         print(f"make: {self.make}, model: {self.model}, color: {self.color}")

#     def cir(self, length):
#         return 2 * car.pi * length

#     def override(self):
#         print("over ride of a car class")

#     def altered(self):
#         print("altered of car class")

# class ElectricCar(Car):

#     def __init__(self, make, model, motor)
#         self.make = make
#         self.model = model
#         self.motor = motor
#         print(f"make: {self.make}, model: {self.model}, color: {self.motor}")
    
#     def printCarType(self):
#         print("I am an electric car")

#     def override(self):
#         print("over ride of electric car class")

#     def altered(self):
#         print("BEFORE altered of elctric car class")
#         super(ElectricCar, self.altered()):
#         print("AFTER altered of electric car class")

    

# ec = ElectricCar("tesla", "s", "red")

# ec.printCarType()

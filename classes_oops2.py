#Inheritance

#Parent class
# class Parent:
#     #class variables
#     a=10
#     b=1000
#     #class methods
#     def doThis(self):
#         print("Do this")
#     def doThat(self):
#         print(DoThat)
# #Child class inheriting Parent class
# class Child(Parent):
#     #child variables
#     a=100
#     b=1000
#     def doWhat(self):
#         print("Do What")
#     def doNotDoThat(self):
#         print("Do not do that")
# parentobj=Parent()
# childobj=Child()
# childobj.doThis()
# childobj.doWhat()
# parentobj.doWhat()

#Animals- mammal and amphibians
# class Animal:
#     #properties
#     multicellular=True
#     eukaryotic=True
#     #functions
#     def breathe(self):
#         print("Breathing")
#     def feed(self):
#         print("Feeding")
#
# class Mammal(Animal):
#     #properties
#     haveMammaryGland=True
#     WarmBlood=True
#     #functions
#     def produceMilk(self):
#         print("Produce Milk")
#
# class Amphibian(Animal):
#     #properties
#     liveInWater=True
#     #functions
#     def metamorphosis(self):
#         print("Metamorphosis")
# Frog=Amphibian()
# Frog.breathe()
# Frog.metamorphosis()
# print(Frog.liveInWater)
#
# Dolphin=Mammal()
# Dolphin.produceMilk()


#Multiple Inheritance
# class A:
#     a=100
# class B:
#     b=200
# class C(A,B):
#     c=300
# c_obj=C()
# print(c_obj.a)
# print(c_obj.b)
# a_obj=A()
# print(a_obj.c)


#Multi-level Inheritance
# class A:
#     a=100
# class B(A):
#     b=200
# class C(B):
#     c=300
# a_obj=A()
# b_obj=B()
# c_obj=C()
# print(a_obj.a)
# print(b_obj.a)
# print(c_obj.a)

#Encapsulation

# class Car:
#     def __init__(self):
#         self.__updateSoftware
#     def drive(self):
#         print('Driving')
#     def __updateSoftware(self):
#         print('Updating Software')
# redcar=Car()
# redcar.drive()
# redcar.__updateSoftware()
# redcar._Car__updateSoftware()


# class Car:
#     __maxspeed=0
#     __name=""
#     def __init__(self):
#         self.__maxspeed=200
#         self.__name="Supercar"
#     def drive(self):
#         print("Driving max speed",str(self.__maxspeed))
# redcar=Car()
# redcar.drive()
# redcar.__maxspeed=100
# redcar.drive()



#Class method and static method

# from datetime import date
#
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @classmethod
#     #class method to create a person object by birthyear
#     def fromBirthYear(cls,name,year):
#         return cls(name,date.today().year-year)
#     #static method to check is a person is an adult or not
#     @staticmethod
#     def isAdult(age):
#         return age>18
#
# person1=Person("Alice",25)
# person2=Person.fromBirthYear("Alice",1993)
# print(person1.age)
# print(person2.age)
# print(Person.isAdult(23))

#Polymorphism

# class Shark:
#     def swim(self):
#         print("The shark is swimming")
#     def swim_backward(self):
#         print("The shark cannot swim backwards, but sink backwards")
#     def skeleton(self):
#         print("The shark's skeleton is made of cartilage")
# class Clownfish:
#     def swim(self):
#         print("The clownfish is swimming")
#     def swim_backward(self):
#         print("The clownfish can swim backwards")
#     def skeleton(self):
#         print("The clownfish's skeleton is made of bone")
#
# def in_the_pacific(fish):
#     fish.swim()
#
# sharky=Shark()
# # sharky.skeleton()
# clowny=Clownfish()
# # clowny.skeleton()
#
# # for fish in (sharky,clowny):
# #     fish.swim()
# #     fish.swim_backward()
# #     fish.skeleton()
# #
# in_the_pacific(sharky)
# in_the_pacific(clowny)



















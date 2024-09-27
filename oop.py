# Procedural to functional moved-:

# Function - Redendancy decrease
#           - Reusability increase

# Now move to object oriented programing:
# more redendandancy and also resubility


# OOP:::
# object banane ke liye phale class banani parti hai or class: iska matlab ye ek blueprint hai


# Class is a blueprint for creating objects.
# Creating class:
# class Student:
#     name = "Karan"

# # Creating object (instance)
# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)


# class Car:
#     color = "pink"
# car1 = Car()
# print(car1.color)


# __init__ Function 
# Constractor== All classes have a function called __init__() , which is always executedd when the object is being initiated.

# creating-
# class Student:
#     name = "muki"
#     def __init__(self): # hame ek self parameter dena hoga
#         print(self)
#         print("adding new student in Database")
    
# s1 = Student()


# class Student:
   
#     def __init__(self, full_name): # hame ek self parameter dena hoga
#        self.name = full_name
#        print("adding new student in Database")
    
# s1 = Student("mjuki")
# print(s1.name)

# s2 = Student("bishnoi")
# print(s2.name)

## self is parameter is a reference to the current instance of the class , and is used to acces variables that belongs to the class

# attributes == variables = name*


# class Student:

#     college_name = "htm school" ## class attributes
#     def __init__(self, name , marks): # hame ek self parameter dena hoga
#        self.name = name
#        self.marks = marks
#        print("adding new student in Database")
    
# s1 = Student("mjuki",23)
# print(s1.name, s1.marks)

# s2 = Student("bishnoi",23)
# print(s2.name, s2.marks)
# print(s2.college_name)

# there are two type of constractors ---- 1. Default 2.parameter constractors



#### class and instance attributes:::: attributes= variables


#### Methods ###:::
# Methods are function that belong to objects.

# class Student:

#     college_name = "htm school" ## class attributes
    
#     def __init__(self, name , marks): # hame ek self parameter dena hoga
#        self.name = name
#        self.marks = marks
#        print("adding new student in Database")
       
    
#     def wlecome(self):
#         print("welcome student", self.name)
     
#     def get_marks(self)    :
#         return self.marks
    
# s1 = Student("muki",23)
# s1.wlecome()
# print(s1.get_marks())



# class Student:
#     def __init__(self, name, marks):
#         self.name= name
#         self.marks = marks
    
#     def get_avg(self)   :
#         sum = 0
#         for val in self.marks:
#             sum+=val
#         print("hi" , self.name , "avg score is", sum/3)
        
# s1 = Student("muki", [90,23,55])
# s1.get_avg()
        


## Static methods::
# dont'use self parameter(woek at class level)

# class Student:
#     @staticmethod # decorator
#     def college():
#         print("muki")

# s1 = Student()
# s1.college()


# important::
# Abstraction # 2. Encapsulation : 3. Inheritantance # 4. Polymorphism

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.accountno = acc
#     #debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount,"was debited")
#         print("total balanced =", self.get_balanced())
        
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("total balanced =", self.get_balanced())
    
#     def get_balanced(self):
#         return self.balance
# acc1 = Account(1000, 123)

# acc1.debit(1000)
# acc1.credit(200)

# del keyboard:
# # used to delete object properties or object itself.

# class Student:
#     def __init__(self, name):
#         self.name = name
        
# s1 = Student("mukesh")
# del s1


# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass # private ::
#     def reset_password(self):
#         print(self.__acc_pass)

# acc1 = Account("134", "mukie9")

# print(acc1.acc_no)
# print(acc1.reset_password())


# Inheritance::::::
# when one class(child/derive) derives the properties and method of another class(parent/base).

# class car:
#     @staticmethod
#     def start():
#         print("car started..")
    
#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(car): # inheritance
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("fortuner")     
# car2 = ToyotaCar("prius")
# print(car1.name)
# print(car2.start())


# # mutiple inheritance :
# class A:
#     print("welcome to here")
# class B:
#     print("hi no welcome here man ")
    
# class C(A, B):
#     print("Welcome back!")
    
# c1 = C()

# class A:
#     def method_from_A(self):
#         print("Method from class A")

# class B:
#     def method_from_B(self):
#         print("Method from class B")

# class C(A, B):
#     def __init__(self):
#         super().__init__()  # Calls the constructor of class A, as it appears first in the inheritance list

# c1 = C()
# c1.method_from_A()  # Output: Method from class A
# c1.method_from_B()  # Output: Method from class B



class car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(car): # inheritance
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
car1 = ToyotaCar("mursris","desil")
print(car1.type)
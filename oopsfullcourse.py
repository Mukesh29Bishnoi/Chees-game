# instance = an object created from the class.
#  class ~= abstract

# class House:
    
#     def __init__(self, price):
#         self.price = price  # self  = instance that is being is created # .price attribute and =  price parameter
        

# class BackPack:
    
#     def __init__(self):
#         self.items = []
        
# classes define the state and the behavior of the  object in  a generic way.

# purpose of the self = self is  a generic way of refering to the current instance of the class.

# class BackPack:
    
#     def __init__(self, item, name):
#         self.item = item
#         self.name = name
#         print(self.item)
#         print(self.name)
#         print(self)
# my_backpack = BackPack(23, "muki")

# Access Instance Attributes::
# in the class:; dot notation = syntax used to acess the members of an object(its variables and methods).

# in class = self.<attributes>
# class BackPack:
    
#     def __init__(self, item, name):
#             self.item = item
#             self.name = name
#             print(self.item)
#             print(self.name)
#             print(self)
# my_backpack = BackPack(23, "muki")


# outside the class::
# <object>.<attribute>
# class BackPack:
    
#     def __init__(self, item, name):
#             self.item = item
#             self.name = name
            
# my_backpack = BackPack(23, "muki")

# print(my_backpack.item)

# default Arguments::: Default values assigned to parameters when their corresponding arguments are omitted,
# # <parameter>= <value>

# class Circle:
#     def __init__(self, radius=3): # here not use space for radius = 3 it is worng
#         self.radius = radius
#         print(self.radius)
        
# my_circle = Circle(788)


# class Circle:
#     def __init__(self, radius=3, color):
#         self.radius = radius
#         self.color = color
#         print(self.radius)
        
# my_circle = Circle(788, "red")



# class Circle:
#     def __init__(self, color):
        
#         self.color = color
        
        
# my_circle = Circle( "red")
# your_circle = Circle("blue")


# print(my_circle.color)
# print(your_circle.color)

# print("changing the color:")
# # udating outside the class
# my_circle.color = "Green"
# your_circle.color = "pink"

# print(my_circle.color)
# print(your_circle.color)   #==== each object is independent from each other...



# class attributes:: it is attributes of the class.
# All instances of the class have acess to the attribute. They share the same value, so any changes made to his value affect all instances.

# define class atributes;:
# <class_attribute> = <value>
# define before the __init method

# class Dog:
#     spieces = "Canis lupus"
    
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
        
# class BackPack:
#     max_num_item = 10
    
#     def __init__(self) -> None:
#         pass
    
#     # accessing the class attributes
# class Dog:
#     spieces = "Canis lupus"
    
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
      
# a = Dog("jin", 13, "German")
# print(a.spieces)
# print(Dog.spieces)

# accesing inside the classs

# class Movie:
#     id_counter = 1
    
#     def __init__(self, title, rating):
#         self.id = Movie.id_counter  # this how it can be do the access
#         self.title = title
#         self.rating = rating
        
#         Movie.id_counter +=1
        
# my_movie = Movie("mission imposible", 4.5)
# your_movie = Movie("James bond", 4.9)

# print(my_movie.id)
# print(your_movie.id)


# How to update the value of class attributes.
# changing the value of class attribute will affect all instances of the class.
# <className>.<class_attribute> = <new_value>

# class Circle:
#     radius = 5
    
#     def __init__(self, color) -> None:
#         self.color = color

# print(Circle.radius)

# my_circle = Circle("Blue")
# your_circle = Circle("Green")

# print(my_circle.radius)
# print(your_circle.radius)

# Circle.radius =10

# print(my_circle.radius)
# print(your_circle.radius)
# print(Circle.radius)


## key principle == Encapsulation and Abstraction

# Encapsulation = Bundling of data and methods that act on that data ito a single unit (class)
# information hidding , serve as shied
# prenvent direct access to the attributes in order to avoid making potentially problematic changes to the state.
# what the developer of the class chose to make public.
# Getters + Setters

## Abstraction = Show only the essential attributtes and hidde unnecessary deatails from the user.
# hide the complexity from the user

# class has two part 1. interface 2. implemention
# interface = visible part oof the class
# implemention = the internal part of the class with the code thet performs the functionality.
# Abstraction also allow us to abstract out common part of the code to avoid repetition


# Attributes = 1. Public  2. Non-public
# Public Attributes = An attributes that can be accessed and modify directly without access restrictions.
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.module = model
#         self.year = year

# my_car = Car("Porsch", "911 carrera", 2020)

# print(my_car.year)
# my_car.year = 300
# print(my_car.year)


## Non-Public Attribute = An attribute that shouldn't be accessed or modifed outside of the class.
# Non-public = 1. by convention = _<attributes>
#               2. changing name = __<attributes> only for special case
#self._<attributes>

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.module = model
#         self._year = year # n9t public

# my_car = Car("Porsch", "911 carrera", 2020)

# print(my_car.year)

# documentation = we don't use term "private" here, since no attributes is really private in python

# class Student :
#     def __init__(self, student_id, name, age, gpa):
#         self.student_id = student_id
#         self.name = name
#         self._age = age
#         self.gpa= gpa

# student = Student("29f","Miki", 43, 7.6 )
# print(student._age)
    

# Name Mangling = process of which the name of the attributes is modified.
# class Student :
#     def __init__(self):
#         self.__id = []

# student = Student()
# print(student._Student__id)  # this is for accessing mangling

# # Properties, Getters, and Setters ##

# Getters and setters are member of class (methods), Getters and setters let us get and set the value of an instance attribue.
# getters = get the value of the attribute.
#Setters = set the value of the attribute.
# they protect the attributes by providing an indirect way to access the and modify them.

# formation = get_ + <attribute>
# Exaples = get_name , get_address, get_color

# class Movie:
#     def __init__(self, title, rating):
#         self._title = title
#         self._rating = rating
        
#     def get_title(self):
#         return self._title
    
# my_movie = Movie("ram", 44)
# print(my_movie.get_title())


# <object>.get_<attribute>()

# Setters in python = Methods that we can call to set the value of an instance attribute.
# With setter we can validate the new value before assigning it to the attribute.
# set_name , set_address etc....


# class Dog:
    
#     def __init__(self, name, age):
#         self._name = name
#         self.age = age
        
#     def get_name(self):
#         return self._name
    
#     def set_name(self, new_name):
#         if isinstance(new_name, str) and new_name.isalpha():
#             self._name = new_name
#         else:
#             print("Please enter a valid name.")
            
# my_dog = Dog("Jacky", 33)
# print("My dog is", my_dog.get_name())

# my_dog.set_name("Jhony44")

# print("My dog is", my_dog.get_name())


# class BackPack:
#     def __init__(self) -> None:
       
#         self._items = []
    
#     def get_items(self):
#         return self._items
    
#     def set_items(self, new_items):
#         if isinstance(new_items, list):
#             self._items = new_items
#         else:
#             print("enter valide value")
    
# b = BackPack()
# print(b.get_items())
# b.set_items(["jami", "james"])
# print(b.get_items())



# property function

# class Dog:
#     def __init__(self, age):
#         self._age = age
        
#     def get_age(self):
#         print("getter is calling")
#         return self._age
    
#     def set_age(self, new_age):
#         print("setter is calling")
#         if isinstance(new_age, int) and 0 < new_age < 30:
#             self._age = new_age
#         else:
#             print("write valide input:")
            
#     age = property(get_age, set_age)
    
    
# my_dog = Dog(5)

# print(f"my dog is {my_dog.age} year old")
# print("one year later")

# my_dog.age +=1
# print(f"my dog age is {my_dog.age} is year old")

# class Circle:
#     VALID_COLOR = ("RED", "GREEN", "YELLOW")
#     def __init__(self, radius, color):
#         self._radius = radius
#         self._color  = color
    
#     def get_radius(self):
#         return self._radius 
    
#     def set_radius(self, new_radius):
#         if isinstance(new_radius, int) and 0 < new_radius :
#             self._radius = new_radius
         
#         else:
#             print("invalide input")
            
#     radius = property(get_radius, set_radius)
            
#     def get_color(self):
#         return self._color
    
#     def set_color(self, new_color):
#         if new_color in Circle.VALID_COLOR:
#             self._color = new_color
        
#         else:
#             print("Enter the valid name of colors")
            
#     color = property(get_color, set_color)
        

    
    
            
# circle = Circle(45, "blue")
# print(f"the vale of radius is : {circle.radius}")

# print("After updating the value")
# circle.set_radius(45)
# print(f"the vale of radius is : {circle.color}")

# print(circle.color)



# Decorator:: a function that takes a function and extends is behavior without expliity modifying it.
# Getter defined ::
# @property
# def property_name(self):
#     return self._property_name

# class Movie:
#     def __init__(self, title, rating):
#         self.title = title
#         self._rating = rating
    
#     @property
#     def rating(self):
#         print("calling the getter")
#         return self._rating
    
#     @rating.setter
#     def rating(self,new_value):
#         print("calling the setter")
#         if 1.0 <= new_value <= 5.0:
#             self._rating =new_value
#         else:
#             print("write a valide input")
        

# fav_mov = Movie("Mad Max", 5)
# print(fav_mov.rating)
# fav_mov.rating = 3
# print(fav_mov.rating)

# setter = @property_name.setter
            # def property_name(self, new_value):
            #     self._property_name = new value

# class BackPack:
#     def __init__(self):
#         self._item = []
        
#     @property
#     def items(self):
#         return self._item
    
#     @items.setter
#     def items(self, new_item):
#         if isinstance(new_item, list):
#             self._item = new_item

# b = BackPack()            
# print(b.items)

# b.items= ["muki", "james"]
# print(b.items)


# Introduction to methods in Python:::
# The method defined in a class determine the behavior of the object created from the class and how they can interect with their state.

# Three type of methods - 1. Instance 2. class 3. static 

# Instance Methods = that belong to a specific object
# they have access to the state of the object that calls them.

#The method defined in a class determine the behavior of the object created from the class and how they can interect with their state.

# Three type of methods - 1. Instance 2. class 3. static 

# Instance Methods = that belong to a specific object
# they have access to the state of the object that calls them.

# class Backpack:
    
#     def __init__(self):
#         self._items = []
        
#     @property
#     def items(self):
#         return self._items
    
#     def add_item(self, item):
#         if isinstance(item, str):
#             self._items.append(item)
            
#         else:
#             print("invalid input")
    
#     def remove_item(self, item):
#         if item in self._items:
#             self._items.remove(item)
            
#         else:
#             return 0
        
#     def has_item(self, item):
#         return item in self._items and True
    
#     def show_items(self, sorted_list=False):
#         if sorted_list:
#             print(sorted(self._items))
            
#         else:
#             print(self._items)
            
    
    
# b = Backpack()

# print(b.items)
# b.add_item("pencil")
# b.add_item("copy")
# print("Not Sorted:")
# b.show_items()
# print("Sorted")
# b.show_items(True)
# print(b.items)
# print(b.has_item("copy"))
# b.remove_item("copy")
# print(b.items)




# HOW to call Method:

# my_list = [3, 4 , 4]

# my_list.append(34)
# my_list.sort()
# my_list.extend([4, 6, 6])
# my_list.sort()
# print(my_list)

# num = my_list.pop() # Gives the last value and also removed by the list
# print(num)
# print(my_list)

# class Circle:
    
#     def __init__(self, radius) -> None:
#         self.radius = radius
        
#     def find_diameter(self):
#         return self.radius*2
    
# my_circle = Circle(4)

# print(my_circle.find_diameter())
        
        
#Default Arguments in Methods

# class Player:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def move_up(self, change=5):
#         self.y += change
        
#     def move_down(self, change=3):
#         self.y -= change
        
#     def move_right(self, change=2):
#         self.x += change
        
#     def move_left(self, change=100):
#         self.x -= change
        
# my_player = Player(8, 7)
# my_player.move_down()
# print(my_player.y)

# my_player.move_up()

# print(my_player.y)

# my_player.move_right()
# print(my_player.x)

# my_player.move_left(5) # we can change custom value::
# print(my_player.x)




# HOw to call methods from  other Methods;::

# Reuse functionality that you already imlemented in the class

# Method A:
# self.method_b(<arguments>)


# class Backpack:
    
#     def __init__(self):
#         self._items = []
        
#     @property
#     def items(self):
#         return self._items
    
#     def add_multiple_items(self, items):
#         for item in items:
#             self.add_item(item) ### calling a method form the another method:: we use self.
            
    
#     def add_item(self, item):
#         if isinstance(item, str):
#             self._items.append(item)
            
#         else:
#             print("invalid input")
    
#     def remove_item(self, item):
#         if item in self._items:
#             self._items.remove(item)
            
#         else:
#             return 0
        
#     def has_item(self, item):
#         return item in self._items and True
    
#     def show_items(self, sorted_list=False):
#         if sorted_list:
#             print(sorted(self._items))
            
#         else:
#             print(self._items)
            
    
    
# b = Backpack()

# b.add_multiple_items(["watter", "candy","balade" ])
# print(b.items)



####  Aggregation ####
 # --- Concept in object - orinted programing that described the relationship between two classes.
 # - Building complex objects that are composed of other objects.
 
 # instance of A ==  instance of B:
 # we store instances of the simpler objects in the more complex objects.
 # it a "has a" relationship between the classes . An object of class B has an object of class A.
 
# class Vehicle:
    
     
#     def __init__(self, color, license_plate, is_electric):
#         self.color = color
#         self.lincense = license_plate
#         self.is_electric = is_electric
         
         
#     def show_license_plate(self):
#         print(self.lincense)
         
#     def show_info(self):
#         print("My vehicle:")
#         print(f"color: {self.color}")
#         print(f"License plate: {self.lincense}")
#         print(f"Electric vehicle {self.is_electric}")
        
        
# class Employee:
    
#     def __init__(self, name, vechile):
#         self.name = name
#         self.vehicle = vechile
    
#     def show_vehicle_info(self):
#         self.vehicle.show_info()
        

# vehicle = Vehicle("black"," 889ne", is_electric=False)
# employee  = Employee("jacky", vehicle)

# print(employee.vehicle)

# employee.show_vehicle_info()

# print("we can do it separadl")
# print(employee.vehicle.color)



# Project of Dice Game:


# ======Objects in Memory::=======
# in python everything is an object.

# print(5, object)

# print(isinstance([1, 2, 3], object))

# print(isinstance((1,2,3), object)) # tuple is instance of object

# print(isinstance("hellow", object)) # hllow is an instance of object

# print(isinstance(True, object))

# def f(c):
#     return c*2
# print(isinstance(f, object))

# class Movie:
    
#     def __init__(self, title):
#         self.title = title
        
# print(isinstance(Movie, object))


# program keeo trck of hoe namy "references" to the  object exist.
# Refrece = name that refers to the location in memory of the obects.
# variable in pytho  store refrences to object in memory.


# The ID() function in the python::

# this fuction returns the address of the object in memory.
# print(id(15))
# print(id("hello world"))

# a = [1, 2, 2]
# b = [1, 2, 2]
# print(id(a))
# print(id(b))


# class Backpack:
    
#     def __init__(self):
#         self._items = []
        
#     @property
#     def items(self):
#         return self._items

# my = Backpack()
# your = Backpack()

# print(id(Backpack()))

# print(id(my))

# print(id(your))

# print(my is your)
# print(my == your)



# "is " operator 
# # if two variables do not referece the same object , they will have different ids.

# a = [3, 4,4 ]
# b = a
# print(b is a)


# a = 257
# b = 257

# print( a is b)

# a = "hi"
# print(id(a))

# b = "hi"
# print(id(b))





# in python objects are passed by reference.
# we pass a reference to the object not a new copy so the original objejct can be modified.

# my_list = [3, 4, 4, 6]
# print("outside the id", id(my_list))

# def print_data(seq):
#     print("inside the id", id(my_list))
#     for ele in seq:
#         print(ele)
        
# print_data(my_list) # we are passing list object that we defined and this object is passed by refrence.

# class Sales:
    
#     def __init__(self, amount):
#         self.amount = amount
        
# def find_total(sales_list):
#     total = 0
    
#     for sale in sales_list:
#         print("new sales")
#         print(sale.amount)
#         total += sale.amount
#     return total

# january_sales = [Sales(400), Sales(4), Sales(10)] # list of objects

# print(find_total(january_sales))
# class Sales:
    
#     def __init__(self, amount):
#         self.amount = amount
        
# def find_total(sales_list):
#     total = 0
    
#     for sale in sales_list:
#         print("new sales")
#         print(sale.amount)
#         total += sale.amount
#     return total

# january_sales = [Sales(400), Sales(4), Sales(10)] # list of objects

# print(find_total(january_sales))



# Aliasing in Python::
# Alias = two or more references to the same memory address in the program.

# a = [3, 4, 4]
# b = a
# c = b #  are alias referecning same objects
# print(id(a))
# print(id(b))
# print(id(c))
# # that means they are alias..





# Mutability and Immutability in Python


# Mutation = change - a significant 
# can be modified.
# Examples = lists, sets, Dictionaries
# a = [3, 4, 5 ]
# a[2] = 9
# print(a)

# Immutation = no change
# can't modified.
# Example = tuples, integers, floats, string

# a = (3, 4, 5 )
# a[2] = 9
# print(a)

# a = "Hello, world!"
# a[0] = "S"
# print(a)

# def add_absolute_value(seq):
#     for i in range(len(seq)):
#         seq[i] = abs(seq[i])
#     return sum(seq)

# value = [-3, -4, -6]
# print("before", value)
# print(add_absolute_value(value))

# print(value)


# a = (1, 3, 4 , 3)

# a = a[:2] + (7,) + a[2:]
# a = a[:1] + (8,4) + a[2:]
# print(a)

# def remove_even_values(dictionary):
#     for key, value in dictionary.copy().items():  # it create a copy of dictionary
#         if value%2 ==0:
        
#             del dictionary[key]
            
# my_dictionay = {"a":1, "b": 2, "c": 3, "d":4}

# remove_even_values(my_dictionay)
# print(my_dictionay)

# cloning in python - creating an exact copy of the object that is completely independent from the orignal object.

# a = [1, 4, 5 ,6]
# b = a[:] # this how to create a clone in python

# b[0] = 15
# print(a)
# print(b)






# inheritance in Python
# Defining class than inherit attributes and methods from other classes.
# Advantages = Reduce code repetition
#Reuse code , Improve readability
# = Classes usually inherit from more genral classes that represent more abstract concepts
# we represent common functionality in the parent class. We add new functionlity or customize the exiting one in the child class
# A class can inherit from multiple classes and multiple classes can inherit from the same class.


# class Polygon:
    
#     def __init__(self, num_sides, color):
#         self.num_sides = num_sides
#         self.color = color
        

# class Triangle( Polygon):
#     pass
    
# my_triangle = Triangle(4, "Black")
# print(my_triangle.color)
 
 
# Main = If the subclass has its own __init__() mehtod, the attributes of the superclass are not inherited automatically.
# class Polygon:
    
#     def __init__(self, num_sides, color):
#         self.num_sides = num_sides
#         self.color = color
        

# class Triangle( Polygon):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
        
    
# my_triangle = Triangle(4, "Black")
# print(my_triangle.color)
###  Solution this problem is = <suprerclass>.__init__(self, <arguments>)

# class Polygon:
    
#     def __init__(self, num_sides, color):
#         self.num_sides = num_sides
#         self.color = color
        

# class Triangle( Polygon):
#     Num_SIDES = 3
#     COLOR = "green"
#     def __init__(self, base, height, color):
#         Polygon.__init__(self, Triangle.Num_SIDES, color)
#         self.base = base
#         self.height = height
        
    
# my_triangle = Triangle(4, 5, "Black")
# print(my_triangle.color)
# print(my_triangle.num_sides)

# Example::
 
# class Employee:
    
#     def __init__(self, full_name, salary):
#         self.full_name = full_name
#         self.salary = salary
        
# class Programer(Employee):
    
#     def __init__(self, full_name, programing_language, salary):
#         Employee.__init__(self, full_name, salary)
#         self.programing_language = programing_language
        
# me = Programer("Mukesh Bishnoi", "Python", 0)
# print(me.full_name, me.programing_language, me.salary)

# Example 2

# class Character:
    
#     def __init__(self, x, y, num_lives):
#         self.x = x 
#         self.y = y
#         self.num_lives = num_lives
        
# class Player(Character):
#     INITAL_X = 0
#     INITAL_Y = 0
#     INITAL_NUM_LIVES = 10
    
#     def __init__(self, score=0):
#         Character.__init__(self, Player.INITAL_X, Player.INITAL_Y, Player.INITAL_NUM_LIVES)
#         self.score = score
    
# class Enemy(Character):
#     def __init__(self, x=15, y=15, num_lives=8, is_positon=False):
#         Character.__init__(self, x, y, num_lives)
#         self.is_positon = is_positon
# player = Player()
# print(player.score)
# print(player.x)
# print(player.num_lives)

# easy_enemy = Enemy(num_lives=1)
# hard_enemy = Enemy(num_lives=15, is_positon=True)

# print(easy_enemy.is_positon, easy_enemy.num_lives)
# print(hard_enemy.is_positon, hard_enemy.num_lives)

# # # inheritance int the python

# class Polygon:
#     def __init__(self, num_side, color):
#         self.num_side = num_side
#         self.color = color
        
#     def describe_polygon(self):
#         print(f"This polygon has {self.num_side} and it's color is {self.color}")
        
# class Square(Polygon):
#     Num = 8
#     def __init(self, base,  color):
#         Polygon.__init__(self, Square.Num, color)
      
#         self.base = base
#         self.color = color
        
# sqare = Square(10,  "black")
# print(sqare.describe_polygon())


# method overriding##
# To prevail over. To neutralize the action of.
# Used to customize or extend the functionality of a method that is alredy defined in the superclass.

# class Teacher:
    
#     def __init__(self, full_name, teacher_id) :
#         self.full_name = full_name
#         self.teacher_id = teacher_id
    
#     def welcome_student(self):
#         print(f"Welcoeme to class ! I'am your teacher. My name is {self.full_name}")
        

# class ScienceTeacher(Teacher):
    
#     def welcome_student(self):       #### this methods is call not the parent class
#         print("hi there how is your day today!")

# scienceTeacher = ScienceTeacher("mukesh bishnoi", 1451)
# print(scienceTeacher.welcome_student())


# there is a method to call same name using = def <method_name>(self):
                                                # <super_class>.<method_name>(self)
                                                

# class Teacher:
    
#     def __init__(self, full_name, teacher_id) :
#         self.full_name = full_name
#         self.teacher_id = teacher_id
    
#     def welcome_student(self):
#         print(f"Welcoeme to class ! I'am your teacher. My name is {self.full_name}")
        

# class ScienceTeacher(Teacher):
    
#     def welcome_student(self):       #### this methods is call not the parent class
#         print("hi there how is your day today!")
#         Teacher.welcome_student(self,)

# scienceTeacher = ScienceTeacher("mukesh bishnoi", 1451)
# print(scienceTeacher.welcome_student())                                                

# another method::
# super().<method_name>(argument) # dont need self argument


#### working with multiple files

# import statment = statment used to get access to the code in another modules.
 
 # Advantages: @ improving project and code organization.
    # @ Grouping related classes , function , and constats.
    # reusing the code in modules.
    
# import <module>
# <module>.<element>
 
# import math
# print(math.pi)

# class Circle:
#     def __init__(self):
#         radius = int(input("enter radius:"))
#         self.radius = radius
        
#     def find_radius(self):
#         area = self.radius*2*math.pi
#         return area

# area = Circle()
# area.find_radius()

# import random

# class Die:
#     def __init__(self) :
#         print(random.randint(1,6))
    
    
# rool_die = Die()

# from module import element

# from math import pi

# from module imort *



# Docstrings::
# importance of writing documanetation

#introduction:: 
# come from two words documentation and strings.
# Docstrings are the string literals that we use to document our code.


# docstrings =                                       # comments
# they are like to element they descrige         # they not liked to any part of the code.

# two type of docstring
# single and multiple docstringd.


# def make_frequency_dict(sequence):
#     """"" Return a dictionary that maps each element in sequence to its frequnecy.
    
#     Creating a dictionary that maps each elements in the list sequence to  the number
#     of times the elements occurs in the list. The element will be the key of the key-value 
#     pair in the dictionary and its frequency will be the value of key pair
    
#     Argument:
#             sequence: A list of values . These value have to be of an immutable data
#             type becuse they will be assigned as keys of the dictionary
            
#     Return:
#             A dictionary that maps each elements in the list to its frequency"""
    
#     if not sequence:
#         raise ValueError("The list cannot be empty")
    
#     freq = {}
    
#     for elem in sequence:
#         if elem not in freq:
#             freq[elem] = 1
        
#         else:
#             freq[elem] += 1
#     return freq

# print(make_frequency_dict([12, 12, 4546, 67])) 

#####@@@

# Special Methods :::
# Megic method also 
# __mthodname__()


# print((5).__add__(6))


# __str()__(self)


# class Point2D:
    
#     def __init__(self, x, y):
#         self.x = x 
#         self.y = y
        
#     def __str__(self):
#         return f"({self.x} , {self.y})"
    
# my_point = Point2D(34,55)
# print(my_point)


# what 



# # __len___()
# my_string = "Hello world!"
# print(len(my_string))
# print(my_string.__len__())

# my_list = [2, 4, 5, 45]
# print(len(my_list))
# print(my_list.__len__())


# Backback class:

class BackPack:
    
    def __init__(self):
        self.items = []
        
    def add_items(self, item):
        self.items.append(item)
    
    def remove_items(self, item):
        self.items.remove(item)
        
    def __len__(self):
        return len(self.items)
        
bagpack = BackPack()
bagpack.add_items("pen")
bagpack.add_items("flowers")
print(len(bagpack))
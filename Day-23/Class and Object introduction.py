# Python is a multi-paradigm programming language. It supports object Oriented Programming (OOP) approach.
# In Python everything is a class.
# Guido Van Rossum has designed the language according to the principle "first-class everything". He wrote: "One of my goals for Python was to make it so that all objects were "fist class". By this, I meant that I wanted all objects that could be named in the language (eg., integers, string, functions, classes, modules, methods and so on) to have qual status. That is, they can be assigned to variables, placed in lists, stored in dictionaries, passed as arguments, and so forth." This means that "everything" is treated the way way, everything is a class: functions and methods are values just like lists, integers or floats. Each of these are instances of their corresponding classes.
# Class is a user-defined type. 
# In OOP, problem is solved by creating objects. 

# Major principle of Object Oriented Programming are:
# 1. Encapsulation
# - Object is an encapsulation of attributes (variables) and behaviors (functions) into a single entity. 
# - This means hiding private details (attribute % behavior) of a class  from other objects. 
# - It is bundling of data with methods which operates on that data. (It does mean that data is hidden)
# - This prevents user from direct modifcation of data. 
# - It is usually accomplished by provding two types of methods called getter method and setter method.
# - Getter method just gets (returns) the values and do not change values of attributes. 
# - Setter method changes the value of attributes. 

# 2. Abstraction
# - This means hiding the complexity and only showing necesaary features of an object.
# - Data Abstraction = Data Encapsulation + Data Hiding
# - Abstraction in Python is implemented using abstract classes and interfaces. 
# - An abstract class provides incomplete behavior and contains one or more abstract methods. 

# 3. Polymorphism
# - This is the concept of using common operation in different ways for different data input. 
# - Polymorphism means one thing having many forms. 
# - When function with same name are used for different data types they are called polymorphism functions in Python. 
# - This is used wgen we have commonly named methods across classes or subclasses in Python. 

# 4. Inheritance
# - This is most important feature of all Object Oriented Programming languages, which was initially introduced for Simula in 1969. 
# - It is the process of using details from new class without modifying existing class. 
# - It is the process of deriving new class from the existing classes. 

# 5. Aggregation
# - It is the concept of linking two logically related objects where one object belongs to the other object. 
# - It shows "has-a" relationship. 
# - Like, address object can be related to employee object and student object. 

# When class is defined, no memory is allocated. 
# Class is a logical entity that contains attribute (variables) and method (function). 
# Attributes and methods created inside the class definition. 
# Method is a function defined inside the class. 
# Method defines the behavior of an instance. 
# We can dynamically create arbitrary new attributes for existing instances of a class, by joining an arbitrary name to the instance name, separated by a dot. 
# Internally, instances possess dictionaries which they use to store thrir attributes and their corresponding values.
# Object is an instantiation of a class, also called instance type class and hence class is also called as blueprint for an object.
# Objects are mutable. 
# Objects is an encapsulation of variables and function into a single entity. 
# Hence class is also called template to create objects. 


# Creating class and object:
# - Python reserved keywords "class" is used to create class. 
# - Class contains class attributes and class methods. 
# - Class attributes are the properties, defined as variable declaration by assigning value. These are also called as instance attributes as they are associated with particular instance and created at runtime. 
# - Class methods reflects behavior or description of object. It describes the functionality defined as class member function. 
# - We can create multiple objects of class. 
# - Each object of class has independent copies of variables defined in the class. 
# - Examples:
# class class_name:
#       attribute_definition
#       method_definition
# object = class_name();


# The self function:
# - In the class definition, there must be some arrangement to represent the instance of that class. 
# - Python provides keywords "self" to represent the class attributes from the class methods. 
# - It is first argument of the __init__ method in every Python class. 
# - When a program is Object Oriented, most of the computation is in terms of operations on object where each object correspond to or represent to some real-world object that interacts through methods. 
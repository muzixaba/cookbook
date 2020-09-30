"""
Four Pillars of OOP (APIE)
Abstraction - Each object is its own idea.
Polymorphism - The ability to have different shapes,(1+1=2, "1"+"1"="11").
Inheritance - Getting features from other objects.
Encapsulation - The ability to lock in certain info within itself.
"""


class Person:
    """
    __init__ is the constructor. Gets run at instance creation
    All Person instances need to be created with a name & gender
    population is a class variable/attribute
    """
    population = "South African"

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        Person.population += 1 # Change class attribute

    def greet(self):
        """
        Instance methods can be applied to instances
        """
        if self.gender == "Female":
            return "Good morning"
        else:
            return "How's it chief!"
    
    @property
    def email(self):
        """
        Assign a method as an attribute
        Similar to df.shape in pandas
        """
        return f"{self.name}.@email.com"

    @classmethod  
    def decrease_population(cls):
        """Class method can access and modify the class state."""
        cls.population -= 1
        return cls.population

    @staticmethod
    def is_adult(age):
        """
        The static method does not take any specific parameter.
        Static Method cannot access or modify the class state
        Normally used to do utility tasks
        """
        return age > 18


#================
# Inheritance
#================
class Mother:
    def __init__(self, eye_color, hair_type):
        self.eye_color = eye_color
        self.hair_type = hair_type.upper()


class Child(Mother):
    """Child gets its eye_color & hair_type from parent"""
    def __init__(self, eye_color, hair_type, name):
        super().__init__(eye_color, hair_type)
        self.name = name


#===============
# Privacy
#==============
class Student:
    def __init__(self, name, surname):
        """No true privacy in python, but can be hinted by using _"""
        self._name = name # _protected
        self.__surname = surname # __private
    
    def get_surname(self):
        """Method created to access private variable"""
        return self.__surname
#!/usr/bin/python3
class Person:
    class_attr = "I am a class attribute"

    def __init__(self, name=None):
        self.name = name
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError("name must be a string")
        self.__name = value

person_1 = Person('Laura')
person_1.class_attr = "This is a changed class attribute"
person_2 = Person('Bob')
print(person_1.__dict__)
print(person_2.__dict__)

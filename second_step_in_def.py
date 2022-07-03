
class Dog(object):
    def __init__(self, name, age):              #__init__ means it is initializing the def, when we call the class(Dog).
        self.name = name
        self.age = age

    def speak(self):
        print('Hi, I am', self.name, 'and I am', self.age, 'years old.')

    def change_age(self, age):
        self.age = age


tim = Dog('Tim', 55)                            # << We have to set the paramenters (name, age) as we like.
fred = Dog('Fred', 3)
tim.change_age(5)
tim.speak()
fred.speak()                                    #< calling the class, they will be now printed out.

print(tim.name, tim.age)

class Cat(Dog):                                 ##< this is called inheritance. Now class Cat will do the same, as the dog class. Instead of copy/pasting it.
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

tim = Cat('tim', 5, 'blue')
tim.speak()
# base class definition
class Adult:
    # initialising base class
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    # prints user is old enough to drive
    def can_drive(self):
        print(f'{self.name} is old enough to drive.')

# subclass of Adult
class Child(Adult):
    def __init__(self, name, age, eye_colour, hair_colour):
        super().__init__(name, age, eye_colour, hair_colour)

    # overriding the base class method
    def can_drive(self):
        print(f'{self.name} is too young to drive.')


def main():
    # user inputs for name, age, hair colour, and eye colour

    name = input("Hi! please enter your name: ")
    correct = False
    # user friendly error handling for possible incorrect input of age (non-numerical inputs)
    while not correct:
        try:
            age = int(input(f'{name} please enter your age: '))
            if type(age) == int:
                if age > 0:
                    correct = True
        except ValueError:
            print(f'Oops! {name} you need to enter an integer that is greater than 0.')

    hair_colour = input('Please enter your hair colour: ')
    eye_colour = input('Please enter your eye colour: ')

    # script
    if age > 17:
        # base class instantiation and method call
        adult = Adult(name, age, eye_colour, hair_colour)
        adult.can_drive()
    else:
        # subclass instantiation and method call
        child = Child(name, age, eye_colour, hair_colour)
        child.can_drive()


# Entry point:
if __name__ == '__main__':
    main()

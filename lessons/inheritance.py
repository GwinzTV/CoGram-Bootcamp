class Vehicle: #base class
    def __init__(self, sound: str) -> None:
        self.sound = sound

    
    def make_sound(self) -> str:
        return f'The {type(self).__name__} goes {self.sound}'
    
    
    def __repr__(self) -> str:
        return f'{type(self).__name__}, noise: {self.sound}'
    
# inheriting everythign from the base class
class Audi(Vehicle): #subclass
    pass



vehicle = Vehicle('vroom').make_sound()
print(vehicle)

audi = Audi('Vroom Vroom!').make_sound()
print(audi)


# == making changes to the sub classes to overide certain methods == #

class Audi(Vehicle):
    def make_sound(self) -> str:
        sound = "The Audi tries to race the other cars!"
        sound += f'{self.sound} {self.sound} {self.sound}'
        return sound
    

audi = Audi('Vroom Vroom!').make_sound()
print(audi)
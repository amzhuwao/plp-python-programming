#usr/bin/python3

"""
    Create a program that includes animals or vehicles with the same action (like move() ).
    However, make each class define move() differently (for example Car.move() prints "Driving" 
    while Plane.move() prints Flying)
"""


class Car():  
    def move(self):
        print(f'Driving')
        
class Plane():
     def move(self):
        print(f'Flying')

bmw = Car()
boeing777 = Plane()

bmw.move()
boeing777.move()
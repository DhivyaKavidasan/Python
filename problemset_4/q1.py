'''
Inheritence example
submitted by :dhivya.kavidasan
date: 10/12/2017
''' 

class Shape:
    def __init__(self):
        pass
    def area(self):
        print(0)
class Square(Shape):
  #subclass extending baseclass
    def __init__(self):
        self.a = a
        pass
    def area(self):
        area=self.a*self.a
        print area
        
a=int(raw_input("enter a length of the square:")) #user's input
obj=Square() #creating object for class
obj.area()   #calling method using object


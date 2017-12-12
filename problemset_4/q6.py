'''
Program to perform temperature converesion
submitted by: dhivya.kavidasan
date: 12/12/2017
'''
class temperature():
    def __init__ (self,temperature):
        self.temperature=temperature
        print "temperature'
	pass
    def aboveFreezing(self):
        pass
    def convertToFahrenheit(self):
        print "inside parent"
        pass
    def convertToCelcius(self):
        pass
    def convertToKelvin(self):
        pass


class fahrenheit(temperature):
    def __init__(self):
        temperature.__init__(self,temperature=int(raw_input("enter the value")))
    def aboveFreezing(self):
        if self.temperature > 0 :
            print "above freezing point"
    def convertToFarenheit(self):
        self.temperature=float((self.temperature*9.0/5.0)+32)
        print "temperature in farenheit is %f" %self.temperature
        

class celsius(temperature):
    def __init__(self):
        temperature.__init__(self,temperature=int(raw_input("enter the value")))
    def convertToCelcius(self):
        self.temperature=float((self.temperature-32)*5.0/9.0)
        print "temperature in celcius is %f" %self.temperature
        return self.temperature
        

a=raw_input("enter the unit of the temperature")
if a=='c' or a=='C':
    obj=fahrenheit()
    obj.convertToFarenheit()
if a=='f' or a=='F':
    obj1=celsius()
    obj1.convertToCelcius()


'''
Inheritence example
submitted by: dhivya.kavidasan
date: 10/12/2017
'''

class Person():
    def getGender( self ):
        return "Unknown"

class Male( Person ):#subclass extending Person
    def getGender( self ):
        return "Male"

class Female( Person ):#subclass extending Person
    def getGender( self ):
        return "Female"

m_obj = Male()
f_obj= Female()
print m_obj.getGender()
print f_obj.getGender()

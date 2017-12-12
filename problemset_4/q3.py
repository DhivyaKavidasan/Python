'''
Description:currency converter
submitted by:dhivya.kavidasan
date:12-12-17
'''
class money:
  def __init__(self,dollars,cents):
    self.dollars=dollars
    self.cents=cents
  def repre(self):
    print "$",self.dollars,".",self.cents
  def add(self,dollars,cents):
    dollars=self.dollars+dollars
    cents=self.cents+cents
    if cents>100:
      dollars=dollars+1
      cents=cents%100
    print "$",dollars,".",cents
  def Indr(self): 
   '''converts dollar to Indian rupee''' 
   d=self.dollars*64.48 
   c=self.cents*0.6448 
   print "Indian_rupee",d+c 
dollars=int(raw_input("dollars"))
cents=int(raw_input("cents"))
a=money(dollars,cents)
a.repre()
a.add(10,5)
a.Indr()

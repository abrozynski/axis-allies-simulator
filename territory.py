from army import *
from installation import *

class territory:
 
 IPCValue = 0
 installations={}


 def __init__(self, territoryname, originalOwner, value):
  self.name=territoryname
  self.originalOwner = originalOwner
  self.owner=originalOwner
  self.IPCValue=value
#  self.armies.append(army(territoryname))
  self.borders=[]
  self.armies={}
  self.territoryType='Land'


# def moveUnit(self, unit, destination):
#  self.army.removeUnit(unit)
#  destination.army.addUnit(unit)

 def addInstallation(self, _type):
  self.installations[_type]=installation(_type,self.name)

 def addArmy(self, armyOwner, enteringArmy):
  if (armyOwner not in self.armies):
   self.armies[armyOwner]=enteringArmy
  else:
   currentArmy=self.armies[armyOwner]
   self.armies[armyOwner]=mergeArmies(currentarmy,enteringArmy)



   



   






  



 












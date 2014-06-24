import copy


# For each unit the following values are recorded
# Attack: when attacking, a die roll <= this value counts as a hit
# Defense: when defending, a die roll <= this value counts as a hit
# Movement: not used here. Will be used in later versions that incorporate movement on the map
# Cost: used to select casualties (cheaper units should be removed first)
# Type: mostly used to make sure land and sea units aren't being mixed. During the BattleRound function, the type may be temporarily overwritten to 'tmp'. This is used to account for the fact that some attack/defense values change during combat without overwriting their unitStats entries

unitStats={'Infantry':{'Attack':1, 'Defense':2, 'Movement':1, 'Cost':3,'Type':'Land'},'Infantry (supported)':{'Attack':2, 'Defense':2,'Movement':1,'Type':'temp'},'Artillery':{'Attack':2, 'Defense':2, 'Movement':1, 'Cost':4,'Type':'Land'},'MechInfantry':{'Attack':2, 'Defense':2, 'Movement':2, 'Cost':4,'Type':'Land'}, 'Tank':{'Attack':3, 'Defense':3, 'Movement':2, 'Cost':5,'Type':'Land'},'AAA':{'Attack':0, 'Defense':0, 'Movement':1, 'Cost':5,'Type':'Land'},'Fighter':{'Attack':3, 'Defense':4, 'Movement':4, 'Cost':10,'Type':'Air'},'Tactical Bomber':{'Attack':3, 'Defense':3, 'Movement':4, 'Cost':11,'Type':'Air'},'Tactical Bomber (supported)':{'Attack':4, 'Defense':3, 'Movement':4, 'Cost':11,'Type':'temp'},'Strategic Bomber':{'Attack':4, 'Defense':1, 'Movement':6, 'Cost':12,'Type':'Air'},'Submarine':{'Attack':2, 'Defense':1, 'Movement':2, 'Cost':6,'Type':'Sea'}, 'Destroyer':{'Attack':2, 'Defense':2, 'Movement':2, 'Cost':8,'Type':'Sea'}, 'Cruiser':{'Attack':3, 'Defense':3, 'Movement':2, 'Cost':12,'Type':'Sea'}, 'Carrier':{'Attack':0, 'Defense':2, 'Movement':2, 'Cost':16,'Type':'Sea'}, 'Battleship':{'Attack':4, 'Defense':4, 'Movement':2, 'Cost':20,'Type': 'Sea'}}
 

nullForce={}
for unit in unitStats:
 if (unitStats[unit]['Type'] != 'temp'):
  nullForce[unit]=0

#The copyArmy function is necessary in order to manipulate an army while still preserving the original

def copyArmy(army):
 return copy.deepcopy(army)


# The army class stores:
#     units -  a dict listing how many of each type of unit are present
#     location - placement on the game board (this will be used when I incorporate movement on the map, which I'm currently working on)

# Functions in the army class
#     addUnit - adds a unit of the given type
#     removeUnit - removes a unit of the given type
#     getUnits - returns the nonzero values of the units dict (it's necessary to continue carrying around the zero elements
#       to prevent key errors during battle simulation
#     getCheapestUnit - self explanatory
#     getMostExpensiveUnit - ditto
#     getBestAttacker - I'll let you use your imagination for these next few
#     getWorstAttacker - 
#     getBestDefender - 
#     getWorstDefender - 
#     move(territory) - changes the location to territory
#     getUnitsOfType - returns the units of the specified type (land/sea/air)


class army:

 units={}
 location='Nowhere'

 def __init__(self, territory, controller='Nobody'):
  self.units=nullForce.copy()
  self.location=territory
  self.owner=controller
 
 def addUnit(self, unit, n=1):
  self.units[unit]+= n

 def removeUnit(self, unit, n=1):
  if (self.units[unit] >= n):
   self.units[unit]=self.units[unit]-n
  else:
   self.units[unit]=0

 def getUnits(self):
  nonZeroUnits={}
  for unit in self.units:
   if self.units[unit] > 0:
    nonZeroUnits[unit]=self.units[unit]
  return nonZeroUnits

 def getCheapestUnit(self):
  if (len(self.getUnits()) != 0):
   costList={}
   for unit in self.getUnits():
    costList[unit] = unitStats[unit]['Cost']
   return min(costList, key=costList.get)
 
 def getMostExpensiveUnit(self):
  if (len(self.getUnits()) != 0):
   costList={}
   for unit in self.getUnits():
    costList[unit] = unitStats[unit]['Cost']
   return max(costList, key=costList.get)

 def getBestAttacker(self):
  if (len(self.getUnits()) != 0):
   attackList={}
   for unit in self.getUnits():
    attackList[unit] = unitStats[unit]['Attack']
   return max(attackList, key=attackList.get)

 def getWorstAttacker(self):
  if (len(self.getUnits()) != 0):
   attackList={}
   for unit in self.getUnits():
    attackList[unit] = unitStats[unit]['Attack']
   return min(attackList, key=attackList.get)

 def getBestDefender(self):
  if (len(self.getUnits()) != 0):
   defenseList={}
   for unit in self.getUnits():
    defenseList[unit] = unitStats[unit]['Defense']
   return max(defenseList, key=defenseList.get)

 def getWorstDefender(self):
  if (len(self.getUnits()) != 0):
   defenseList={}
   for unit in self.getUnits():
    defenseList[unit] = unitStats[unit]['Defense']
   return min(defenseList, key=defenseList.get)

 def move(self, territory):
  self.location = territory

 def getUnitsOfType(self, unitType):
  if (len(self.getUnits()) != 0):
   unitsOfType={}
   for unit in self.getUnits():
    if (unitStats[unit]['Type'] == unitType):
     unitsOfType[unit] = self.units[unit]
   return unitsOfType


 def sumAttack(self):
  totalAttack=0
  for unit in self.units:
   totalAttack += unitStats[unit]['Attack']*self.units[unit]
  return totalAttack

 def sumDefense(self):
  totalDefense=0
  for unit in self.units:
   totalDefense += unitStats[unit]['Defense']*self.units[unit]
  return totalDefense

# Ground state army:

nullArmy=army('Nowhere')

# Command line army input

def simpleArmyInput(location):
 if (location == 1):
  unitType='Land'
 if (location == 2):
  unitType='Sea'

 newForce=army('Nowhere')                                                                              
 for unit in unitStats:
  if unitStats[unit]['Type'] == unitType or unitStats[unit]['Type'] == 'Air':
   print unit
   unitNumber=int(raw_input('-->'))
   if unitNumber >= 0:
    newForce.units[unit]=unitNumber
  elif unitStats[unit]['Type'] != 'temp':
   newForce.units[unit]=0
 return newForce


def mergeArmies(army1,army2):
 if ((army1.owner == army2.owner) and (army1.location == army2.location)):
  army3=army(army1.owner,army1.location)
  for unit in army1.units:
   army3.addUnit(unit, n=army1.units[unit])
  for unit in army2.units:
   army3.addUnit(unit, n=army2.units[unit])
  return army3


  
  
  
  


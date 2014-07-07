from army import *
from territory import *
#from game import territoryDict
from copy import copy

class gameMap:
 
# def getPossibleUnitMoves(self,unit, location):
#  possibleMoves=[]
#  for territory in territoryDict:
#   if (self.measureDistance(location, territory) <= unitStats[unit]['Movement']):
#    possibleMoves.append(territory)
#  return possibleMoves

# def measureDistance(self, startingTerritory, endingTerritory):
#  distance =1
#  checklist = territoryDict[startingTerritory].borders
#  while (endingTerritory not in checklist):
#   for territory in checklist:
#    territoryObj=territoryDict[territory]
#    checklist += territoryObj.borders
#    checklist = list(set(checklist))
#   distance +=1
#  return distance

 def getTerritoriesInRange(self, startingTerritory, n):
  territoriesInRange =[startingTerritory]
  counter = 1
  while (counter <= n):
   nextStep = self.addBorderingTerritories(territoriesInRange, counter)
   territoriesInRange = territoriesInRange + nextStep[0]
   counter = nextStep[1]
  return list(set(territoriesInRange))
  


 def addBorderingTerritories(self, territoryList, counter):
  for territory in territoryList:
   territoryObj=territoryDict[territory]
   territoryList = territoryList + territoryObj.borders
  territoryList = list(set(territoryList))
  counter += 1
  return (territoryList, counter)
  

 def measureDistance(self, startingTerritory, endingTerritory):
  checklist = territoryDict[startingTerritory].borders
  counter = 1
  while (endingTerritory not in checklist):
   newList = self.addBorderingTerritories(checklist, counter)
   checklist = newList[0]
   counter = newList[1]
  return counter


 def getPossibleUnitMoves(self, unit, location):
  unitType=unitStats[unit]['Type']
  possibleMoves = self.getTerritoriesInRange(location, unitStats[unit]['Movement'])
  print possibleMoves
  finalPossibleMoves = copy(possibleMoves)
  if (unitType != 'Air'):
   for territory in possibleMoves:
    if (territoryDict[territory].territoryType != unitType):
     finalPossibleMoves.remove(territory)
  return finalPossibleMoves

 def getFlightPaths(self, unit, takeOffTerritory, battleTerritory, nation):
  possibleLandings=[]
  distanceToBattle = self.measureDistance(takeOffTerritory, battleTerritory)
  if (distanceToBattle < unitStats[unit]['Movement']):
   remainingMoves = unitStats[unit]['Movement'] - distanceToBattle
   allLandings = self.getTerritoriesInRange(battleTerritory, remainingMoves)
   for territory in allLandings:
    territoryOwner = territoryDict[territory].owner
    if ((territoryOwner == nation) or (territoryOwner == 'Poseidon')):
     possibleLandings.append(territory)
  return possibleLandings  

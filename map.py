from army import *
from territory import *
from game import territoryDict

class map:
 
 def getPossibleUnitMoves(self,unit, location):
  possibleMoves=[]
  for territory in territoryDict:
   if (self.measureDistance(location, territory) <= unitStats[unit]['Movement']):
    possibleMoves.append(territory)
  return possibleMoves

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
  territoriesInRange =[]
  


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

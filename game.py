#from army import *
#from territory import *
#from nation import *
import europe1940 as boardSetup
#import gameMap
from army import unitStats, nullArmy

#theboard=boardSetup.boardSetup()
#territoryDict = theboard.territoryDict
#theaters = theboard.theaters


class game:
 

 def __init__(self):
  self.gameBoard=boardSetup.boardSetup()
  self.players=self.gameBoard.players
  self.territoryDict=self.gameBoard.territoryDict


# Methods for measuring distance and moving around on board
  

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
   territoryObj=self.territoryDict[territory]
   territoryList = territoryList + territoryObj.borders
  territoryList = list(set(territoryList))
  counter += 1
  return (territoryList, counter)
  

 def measureDistance(self, startingTerritory, endingTerritory):
  checklist = self.territoryDict[startingTerritory].borders
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
    if (self.territoryDict[territory].territoryType != unitType):
     finalPossibleMoves.remove(territory)
  return finalPossibleMoves

 def getFlightPaths(self, unit, takeOffTerritory, battleTerritory, nation):
  possibleLandings=[]
  distanceToBattle = self.measureDistance(takeOffTerritory, battleTerritory)
  if (distanceToBattle < unitStats[unit]['Movement']):
   remainingMoves = unitStats[unit]['Movement'] - distanceToBattle
   allLandings = self.getTerritoriesInRange(battleTerritory, remainingMoves)
   for territory in allLandings:
    territoryOwner = self.territoryDict[territory].owner
    if ((territoryOwner == nation) or (territoryOwner == 'Poseidon')):
     possibleLandings.append(territory)
  return possibleLandings  


# Taking turns


 def collectIncome(self, nation):
#  for theater in self.gameBoard.theaters.values():
#   if nation in theater.getCombatants():
#    for zone in theater.zones.values():
#     self.players[nation].IPC += zone.getEconomicStandings()[nation]
  for territory in self.territoryDict.values():
   if territory.owner == nation:
    self.players[nation].IPC += territory.IPCValue

#####
#
# DANGER WILL ROBINSON
# 
# Testing the above function shows that something is slightly off in the map initialization
# Germany is short 3 IPCs
# UK is short 2
# USA IS A-OK
# USSR is fine
# france is splendid
# Italy is good
#
# FIX THAT SHIT
#
######


 def purchaseUnit(self, nation, unit, number=1):
 
  self.players[nation].stagedArmy.addUnit(unit, n=number)
  self.players[nation].IPC -= unitStats[unit]['Cost']*number






# Strategery

 def economicComparison(self, theaterName):
  theater = self.gameBoard.theaters[theaterName]
  economies ={'Axis':0,'Allies':0}
  economicStandings = theater.getEconomicStandings()
  for nation in economicStandings:
   if nation in self.players:
    side = self.players[nation].stance
    if side in economies:
     economies[side] += economicStandings[nation]
  return economies

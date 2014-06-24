from army import *
from territory import *
from game import territoryDict

# Broad strategic objectives are organized into theaters.
# Each theater is divided into zones of control

#territoryDict=europe1940.europe1940().territoryDict

class theater:

  def __init__(self, _name, _zones, ):
   self.name=_name
   self.zones=_zones
   
  def getCombatants(self):
   combatants=[]
   for zone in self.zones:
    zoneCombatants = self.zones[zone].getCombatants()
    for nation in zoneCombatants:
     if nation not in combatants:
      combatants.append(nation)
   return combatants
     


class zoneOfControl:

  def __init__(self, _name, _territoryList):
   self.territoryList = _territoryList
   self.name=_name

  def getCombatants(self):
   combatants = []
   for territoryName in self.territoryList:
    territory=territoryDict[territoryName]
    if territory.owner not in combatants:
     combatants.append(territory.owner)
    for key in territory.armies:
     if key not in combatants:
      combatants.append(key)
   return combatants

  def getEconomicStandings(self):
   economicStandings={}
   for nation in self.getCombatants():
    economicStandings[nation]=0
   for territoryName in self.territoryList:
    territory = territoryDict[territoryName]
    economicStandings[territory.owner] += territory.IPCValue
   return economicStandings

  def getOffensivePower(self):
   offensivePower={}
   for nation in self.getCombatants():
    offensivePower[nation]=0
   for territoryName in self.territoryList:
    territory=territoryDict[territoryName]
    for army in territory.armies.values():
     offensivePower[army.owner]+=army.sumAttack()
   return offensivePower
 
  def getDefensivePower(self):
   defensivePower={}
   for nation in self.getCombatants():
    defensivePower[nation]=0
   for territoryName in self.territoryList:
    territory=territoryDict[territoryName]
    for army in territory.armies.values():
     defensivePower[army.owner]+=army.sumDefense()
   return defensivePower


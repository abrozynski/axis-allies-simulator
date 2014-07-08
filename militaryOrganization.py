#from army import *
#from territory import *
#import game
#from game import territoryDict

# Broad strategic objectives are organized into theaters.
# Each theater is divided into zones of control

#territoryDict=europe1940.europe1940().territoryDict

class theater:

 def __init__(self, _name, _zones, _territoryDict):
  self.name=_name
  self.zones=_zones
  self.support={}
  self.territoryDict = _territoryDict
#  self.nation = _nation
  
 def getCombatants(self):
  combatants=[]
  for zone in self.zones.values():
   combatants = combatants + zone.getCombatants()
  return list(set(combatants))

 def getAvailableSupport(self):
  for zone in self.zones:
   for territory in zone.territoryList:
    self.support[territory] = self.territoryDict[territory].armies[nation].getUnitsOfType['Air']


 def getEconomicStandings(self):
  economicStandings = {}
  for nation in self.getCombatants():
   economicStandings[nation]=0
  for zone in self.zones.values():
   zoneStandings = zone.getEconomicStandings()
   for nation in zoneStandings:
    economicStandings[nation] += zoneStandings[nation]
  return economicStandings


 def getOffensivePower(self):
  offensivePowers = {}
  for nation in self.getCombatants():
   offensivePowers[nation]=0
  for zone in self.zones.values():
   zoneStandings = zone.getOffensivePower()
   for nation in zoneStandings:
    offensivePowers[nation] += zoneStandings[nation]
  return offensivePowers
     
     


class zoneOfControl:

 def __init__(self, _name, _territoryList, _territoryDict):
  self.territoryList = _territoryList
  self.name=_name
  self.territoryDict=_territoryDict

 def getCombatants(self):
  combatants = []
  for territoryName in self.territoryList:
   territory=self.territoryDict[territoryName]
   if ((territory.owner not in combatants) and (territory.owner != 'Poseidon')):
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
   territory = self.territoryDict[territoryName]
   if territory.owner != 'Poseidon':
    economicStandings[territory.owner] += territory.IPCValue
  return economicStandings

 def getOffensivePower(self):
  offensivePower={}
  for nation in self.getCombatants():
   offensivePower[nation]=0
  for territoryName in self.territoryList:
   territory=self.territoryDict[territoryName]
   if territory.owner != 'Poseidon':
    for army in territory.armies.values():
     offensivePower[army.owner]+=army.sumAttack()
  return offensivePower
 
 def getDefensivePower(self):
  defensivePower={}
  for nation in self.getCombatants():
   defensivePower[nation]=0
  for territoryName in self.territoryList:
   territory=self.territoryDict[territoryName]
   if territory.owner != 'Poseidon':
    for army in territory.armies.values():
     defensivePower[army.owner]+=army.sumDefense()
  return defensivePower


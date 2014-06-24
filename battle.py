
import numpy
import random
from army import *

def diceRoll():                                                                           
 return 1+int(5.0*random.random())


class battle:
 attacker={}
 defender={}
 
 def __init__(self, inputattacker, inputdefender):
  self.attacker=copyArmy(inputattacker)
  self.defender=copyArmy(inputdefender)

 def battleRound(self, inputattacker, inputdefender):

  attacker=copyArmy(inputattacker)
  defender=copyArmy(inputdefender)


  if ((attacker.units['Infantry'] > 0) and (attacker.units['Artillery'] > 0)):
   if attacker['Infantry'] <= attacker.units['Artillery']:
    for i in range(0, attacker.units['Infantry']):
     attacker.removeUnit['Infantry']
     attacker.addUnit['Infantry (supported)']
   if attacker.units['Infantry'] > attacker.units['Artillery']:
    for i in range(0, attacker.units['Artillery']):
     attacker.removeUnit['Infantry']
     attacker.addUnit['Infantry (supported)']
    
  if ((attacker.units['Tactical Bomber'] > 0) and (attacker.units['Fighter'] > 0)):
   if attacker.units['Tactical Bomber'] <= attacker.units['Fighter']:
    for i in range(0, attacker.units['Tactical Bomber']):
     attacker.removeUnit['Tactical Bomber']
     attacker.addUnit['Tactical Bomber (supported)']
   if attacker.units['Tactical Bomber'] > attacker.units['Fighter']:
    for i in range(0, attacker.units['Artillery']):
     attacker.removeUnit['Tactical Bomber']
     attacker.addUnit['Tactical Bomber (supported)']

  if ((attacker.units['Tactical Bomber'] > 0) and (attacker.units['Tank'] > 0)):
   if attacker.units['Tactical Bomber'] <= attacker.units['Tank']:
    for i in range(0, attacker.units['Tactical Bomber']):
     attacker.removeUnit['Tactical Bomber']
     attacker.addUnit['Tactical Bomber (supported)']
   if attacker.units['Tactical Bomber'] > attacker.units['Tank']:
    for i in range(0, attacker.units['Tank']):
     attacker.removeUnit['Tactical Bomber']
     attacker.addUnit['Tactical Bomber (supported)']  



  attackerHits=0
  for unit in self.attacker.getUnits():
   for i in range(0, attacker.units[unit]):
    roll = diceRoll()
    if (roll <= unitStats[unit]['Attack']):
      attackerHits+=1

  defenderHits=0
  for unit in self.defender.getUnits():
   for i in range(0, defender.units[unit]):
    roll = diceRoll()
    if (roll <= unitStats[unit]['Defense']):
     defenderHits+=1


  nextRoundAttacker = self.removeCasualties(attacker, defenderHits, 'Attack')                                # Call up the removeCasualties function to remove casualties from each army
  nextRoundDefender = self.removeCasualties(defender, attackerHits, 'Defense')  

  return (nextRoundAttacker, nextRoundDefender)

  



 def removeCasualties(self, inputarmy, hits, trait):
  army=copyArmy(inputarmy)
  if (len(army.getUnits()) == 0):
   return army
  if hits > len(army.getUnits()):
   army = copyArmy(nullArmy)
   army.move(inputarmy.location)
   return army
  elif (trait == 'Attack'):
   worstUnit = army.getWorstAttacker()
  elif (trait == 'Defense'):
   worstUnit=army.getWorstDefender()
  for unit in army.units:
   if ((unitStats[unit][trait] == unitStats[worstUnit][trait]) and (unitStats[unit]['Cost'] < unitStats[worstUnit]['Cost'])):
    worstUnit=unit

  if (hits <= army.units[worstUnit]):
   for i in range(0, hits):
    army.removeUnit(worstUnit)
   return army
  if (hits > army.units[worstUnit]):
   spilloverHits = hits - army.units[worstUnit]
   army.units[worstUnit]=0
   return self.removeCasualties(army, spilloverHits, trait)



 def runBattle(self, inputattacker, inputdefender, roundNumber):
  attacker=copyArmy(inputattacker)
  defender=copyArmy(inputdefender)

  if ((roundNumber ==1) and (defender.units['AAA'] > 0)):

   maxAAshots = 3.0*defender.units['AAA']

   AAShots = min(sum(attacker.getUnitsOfType('Air')), maxAAshots)
 
   AAHits = 0
   for i in range(0,AAShots):
    roll = diceRoll()
    if (roll <= 1.0):
     AAHits += 1
 
   postAAAttackingAirUnits=removeCasualties(attacker.getUnitsofType('Air'), AAHits, 'Attack')

   for unit in postAAAttackingAirUnits:
    attacker.units[unit] = postAAAttackingAirUnits[unit]


  battleResult={}
  remainingForces=self.battleRound(attacker,defender)
#  print remainingForces
  if ((sum(remainingForces[0].units.values())>0) and (sum(remainingForces[1].units.values())<=0)):
   battleResult['Victor']='Attacker'
   battleResult['Remaining Attackers']=remainingForces[0]
   battleResult['Remaining Defenders']=copyArmy(nullArmy)
   return battleResult
  if ((sum(remainingForces[1].units.values())>=0) and (sum(remainingForces[0].units.values())<=0)):
   battleResult['Victor']='Defender'
   battleResult['Remaining Attackers']=copyArmy(nullArmy)
   battleResult['Remaining Defenders']=remainingForces[1]
   return battleResult
  else:
   return self.runBattle(remainingForces[0],remainingForces[1], roundNumber+1)
   



 def battleStats(self):
  attackingArmy=copyArmy(self.attacker)
  defendingArmy=copyArmy(self.defender) 


  ntrials=10000.0

  remainingAttackers=[]
  remainingDefenders=[]
  wins=0.0
  for i in range(0,int(ntrials)):
   trialResult=self.runBattle(attackingArmy,defendingArmy,1)
   if (trialResult['Victor'] == 'Attacker'):
    remainingAttackers.append(sum(trialResult['Remaining Attackers'].units.values()))
    remainingDefenders.append(0.0)
    wins+=1.0
   else:
    remainingAttackers.append(0.0)
    remainingDefenders.append(sum(trialResult['Remaining Defenders'].units.values()))
 
  winChance=wins/ntrials
 
  avgSurvivingAttackers=sum(remainingAttackers)/ntrials
  stdSurvivingAttackers=numpy.std(remainingAttackers)
  avgSurvivingDefenders=sum(remainingDefenders)/ntrials
  stdSurvivingDefenders=numpy.std(remainingDefenders)


  return {'Probability of Attacker Victory (1% error)': winChance, 'Attacking Survivors': {'Mean': avgSurvivingAttackers, 'Sigma': stdSurvivingAttackers}, 'Defending Survivors':{'Mean': avgSurvivingDefenders, 'Sigma': stdSurvivingDefenders}}




















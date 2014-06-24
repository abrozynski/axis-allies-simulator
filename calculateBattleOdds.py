#! /usr/bin/python


import numpy
import random
import math
from army import *


# The purpose of this code is to simulate a battle in the board game Axis & Allies (full rules can be found at http://www.wizards.com/AvalonHill/rules/A&A_Europe_1940_2ndEd_Rulebook_LR.pdf).
# The user is asked to input the attacking and defending armies. The program runs the battle many (10000) times and returns the win chance and expected casualty rate.



def diceRoll():                                                                           #seemed useful
 return 1+int(5.0*random.random())



# Class: battle
# Input: attacker and defender (both objects of army class)
# Functions: battleRound - runs one round of battle (attackers and defenders fire and remove casualties), returns survivors
#            runBattle - calls the battleRound function until one side has no units left
#            removeCasualties - this function provides the criteria for selecting the order in which units are chosen as casualties
#            battleStats - simulates many battles and returns the probability of an attacker victory, along with the expected number of remaining units





class battle:                                                            
 attacker={}
 defender={}
 
 def __init__(self, inputattacker, inputdefender):
  self.attacker=copyArmy(inputattacker)
  self.defender=copyArmy(inputdefender)


# Axis and Allies general battle structure:
# Attacker rolls one die for each unit, records hits
# Defender rolls one die for each unit, records hits
# Attacker and defender each remove casualties equal to their opponent's hits
# Lather, rinse, repeat
# End battle when one side has no units left


# BattleRound function:
# this function takes in an attacking and defending army. It runs a single round of battle and returns the surviving attackers and defenders


 def battleRound(self, inputattacker, inputdefender):

  attacker=copyArmy(inputattacker)
  defender=copyArmy(inputdefender)
                                                                                                      # First we need to copy the attacker into a new dictionary with needed tmp entries
                                                                                                      # It's all quite tedious if you're not familiar with the rules.

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



  attackerHits=0                                                                                               # Ok! Here's the fight. First we establish a hit counter
  for unit in self.attacker.getUnits():                                                                        # then one die roll per unit
   for i in range(0, attacker.units[unit]):
    roll = diceRoll()
    if (roll <= unitStats[unit]['Attack']):                                                                    # if the roll <= the unit's attack, then it's a hit
      attackerHits+=1

  defenderHits=0                                                                                              # Do the same for the defenders
  for unit in self.defender.getUnits():
   for i in range(0, defender.units[unit]):
    roll = diceRoll()
    if (roll <= unitStats[unit]['Defense']):
     defenderHits+=1


  nextRoundAttacker = self.removeCasualties(attacker, defenderHits, 'Attack')                                # Call up the removeCasualties function to remove casualties from each army
  nextRoundDefender = self.removeCasualties(defender, attackerHits, 'Defense')  

  return (nextRoundAttacker, nextRoundDefender)

  
# The purpose of the removeCasualties function is to remove casualties. In Axis & Allies, each player gets to choose the order in which casualties are removed. This function decides which units to remove and deletes them from the dictionary.

#It takes as input the army, the number of casualties to be removed, and a trait by wich units are judged. This final input is either 'Attack' or 'Defense' depending on what the army is doing at the time. The idea is that, if you're attacking you'd want your first casualties to be the units that are worst at attacking. In the event of a tie, the cost of each unit is compared and the cheaper one is eliminated.


 def removeCasualties(self, inputarmy, hits, trait):
  army=copyArmy(inputarmy)
  if ((len(army.getUnits()) == 0) or (hits == 0)):
   return army
  if hits > len(army.getUnits()):
   army = copyArmy(nullArmy)
   army.move(inputarmy.location)
   return army
  elif (trait == 'Attack'):
   worstUnit = army.getWorstAttacker()
  elif (trait == 'Defense'):
   worstUnit=army.getWorstDefender()
  for unit in army.getUnits():
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


# The runBattle function takes in an attacking and defending army and calls the battleRound function until one side wins.
# It returns the victor ('Attacker' or 'Defender') and a dictionary listing the surviving units.
# The roundNumber counter is used to track recursions. Its primary use is to account for the fact that anti-aircraft artillery only fire on the first round.
# In future versions the round number counter could be used as a signifier of prediction accuracy. One would expect more one-sided battles to end in fewer rounds


 def runBattle(self, inputattacker, inputdefender, roundNumber):
  attacker=copyArmy(inputattacker)
  defender=copyArmy(inputdefender)

# First we have anti-aircraft. Again, only interesting if you know the rules.


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

# Ok, so after dealing with anti-aircraft we get onto the main event.
# This part is very simple. It just calls the battleRound function until one side has no units

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
   

# drumroll


# Here's where we calculate odds.
# The battleStats() function calls the battle function many times, recording the victor and number of survivors of each trial
# Average over all trials and return the percentage of battles that resulted in an attacker victory and the expected number and standard deviation of survivors for each side.

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

  error=math.sqrt(ntrials)


  return {'Probability of Attacker Victory (1% error)': winChance, 'Attacking Survivors': {'Mean': avgSurvivingAttackers, 'Sigma': stdSurvivingAttackers}, 'Defending Survivors':{'Mean': avgSurvivingDefenders, 'Sigma': stdSurvivingDefenders}}


# And here's the bit that shows up when you run it as an executable


print '\n * Axis & Allies Battle Probability Simulator * \n'
print 'Press 1 if by land, 2 if by sea'                                                  #...and I on the opposite shore shall be
location=int(raw_input('-->'))
print 'Please enter how many of each type of unit are attacking:'
attacker=simpleArmyInput(location)
print '\n'
print 'Please enter how many of each type of unit are defending:'
defender=simpleArmyInput(location)
battle= battle(attacker,defender)
output=battle.battleStats()
print '\n'
for key in output:
 print key, output[key]
print '\n'















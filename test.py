#! /usr/bin/python

from game import *
thegame=game()
denmark=thegame.territoryDict['Denmark']
anarmy=army('Nowhere')
anotherarmy=army('Nowhere')
anarmy.addUnit('Infantry', n=3)
anotherarmy.addUnit('Tank',n=4)


from army import nullArmy

class nation:


 def __init__(self,_name):
  self.name =_name
  self.stance = 'Neutral'
  self.IPC = 0
  self.controlledTerritories=[]
  self.stagedArmy = nullArmy

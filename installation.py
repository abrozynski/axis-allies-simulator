installation_types=['Major IC','Minor IC','Air Base','Naval Base']


class installation:
 
 def __init__(self, _type, _location):
  self.location=_location
  self.installation_type = _type
  self.damage = 0
  self.operable = True

 def addDamage(self, damageRoll):
  self.damage += damageRoll
  if ((self.installation_type == 'Major IC') and (self.damage >= 10)):
   self.operable == False
  elif (self.damage >= 3):
   self.operable == False

  def removeDamage(self, repair):
   self.damage = self.damage - repair
   if ((self.installation_type == 'Major IC') and (self.damage <= 10)):
    self.operable == True
   elif (self.damage <= 3):
    self.operable == True

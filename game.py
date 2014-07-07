from army import *
from territory import *
from nation import *
import europe1940 as boardSetup
import gameMap

#theboard=boardSetup.boardSetup()
#territoryDict = theboard.territoryDict
#theaters = theboard.theaters


class game:
 

 def __init__(self):
  self.gameBoard=boardSetup.boardSetup()
  self.players=self.gameBoard.players
  self.territoryDict=self.gameBoard.territoryDict

  


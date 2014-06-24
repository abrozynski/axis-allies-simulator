Axis and Allies Simulator

Table of Contents:

 Global Variables:
  territoryDict (in game module) - Formatted as {territory name: territory object instance} 
  unitStats (in army module) - Formatted as {unit name: { unit property : value}} (see comments in army.py for more information)

 Classes:

  game - Records all board and player information

  army - Each army instance contains the following attributes:
           - units: Formatted as {unit name: number of units present} (e.g. {'Infantry':3})
           - location: name of the territory where the army is (str)
           - owner: nation that controls the army (str)
       - And the following methods:
           - addUnit(unit name, n = number of units to add): the n variable is optional, with the default n=1
           - removeUnit(unit name, n=number of units to remove)
           - getCheapestUnit(): returns the unit with the lowest cost
           - getMostExpensiveUnit()
           - getBestAttacker(): returns the unit with the highest attack value
           - getWorstAttacker()
           - getBestDefender()
           - getWorstDefender()
           - move(territory): reassigns the location attribute
           - getUnitsOfType(type): returns the number of units of a given type in the army
           - sumAttack(): sums all of the attack values of all units in the army
           - sumDefense()

  battle - A battle is initialized with two input armies and contains the following methods:
           - battleRound(): runs a single round of combat
           - removeCasualties(): selects the order in which units of a given army are lost
           - runBattle(): runs successive rounds of combat until one side has no units left
           - battleStats(): simulates the battle many (10000) times and returns statistics on the results (win chance and expected number of units remaining, with standard deviation of each statistic) 

  europe1940 - Contains the specifics of the board setup for Axis & Allies Europe 1940 Second Edition (everything else can be generalized to other versions of the game). Calling an instance of this object will create a territory object for every territory on the board and write them into a territoryDict (the boardSetup() method). It will initialize the players (initializePlayers() method) and add army objects to each territory according to the board setup (the populateBoard() method). 

  installation - Factories, air bases, and navel bases are represented as instances of this class. Each territory object carries a list of installations present

  nation - Each nation instance contains the following attributes:
           - name (str)
           - stance: Can be 'Allies', 'Axis', 'Neutral', 'Pro-Allies','Pro-Axis'. Used to determine who is fighting whom. The game implications of each stance can be found in the rulebook.
           - IPC: money on hand. Collected at the end of each turn and spent at the beginning of the next turn. Equal to the sum of the IPC values of all controlled territories
           - controlledTerritories: list of the names of all territories controlled by that nation

  territory - Each territory instance contains the following attributes:
                - name (str)
                - originalOwner: owner at the beginning of the game (str)
                - owner: current owner
                - IPCValue: income gained by controlling this territory
                - borders: a list of the names of all territories bordered by this terrritory
                - armies: Formatted as {nation name: army object}. All troops present in the territory
            - And the following methods
                - addInstallation(type): adds a factory, air base, or naval base to the territory
                - addArmy(armyOwner, army object): adds a given army to the territory

  militaryOrganization - This module divides the board into theaters, which are further divided into zones of control. 
       Each theater instance contains the following attributes and methods:
         - name (str)
         - zones - formatted as {zone name: zone of control object}
         - getCombatants() - returns a list of nations present in the theater

        Each zone of control instance contains the following:
         - name (str)
         - territoryList - list of all territories in the zone
         - getCombatants() - returns a list of nations present in the zone
         - getEconomicStandings() - returns the sum of IPC values of territories controlled by each nation in the zone
         - getOffensivePower() - returns the sum of attack values of all units controlled by each nation in the zone
         - getDefensivePower()


An AI instance (I'm still working on this bit) will assign relative importance to each theater based on a prescribed overarching strategy. On a given turn it will examine all possible end of turn board states in each zone and, based on the overarching strategy, select the move that optimizes one of the metrics in the militaryOrganization module. (Ideally, this will calculate two turns ahead and optimize based on that result). For instance, a nation instance named 'USA' might divide the board into theaters named 'Atlantic' and 'Pacific'. An overarching strategy could be 'Attack Germany', in which case the AI would seek to maximize the difference between the American offensive power and the German defensive power in each of the zones in the Atlantic theater. The strategy would then also define a maximum acceptable disparity between Japanese offensive power and American defensive power in the Pacific theater.

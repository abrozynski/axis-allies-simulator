from territory import *
from nation import *
#from army import *
#from installation import *
from militaryOrganization import theater, zoneOfControl

class boardSetup:
 players={}

 def constructBorder(self, territory1, territory2):
  self.territoryDict[territory1].borders.append(territory2)
  self.territoryDict[territory2].borders.append(territory1)


 def buildMap(self):

  self.territoryDict['Alberta Saskatchewan Manitoba']=territory('Alberta Saskatchewan Manitoba', 'UK', 1)
  self.territoryDict['Ontario']=territory('Ontario', 'UK', 2)
  self.territoryDict['Quebec']=territory('Quebec','UK',2)
  self.territoryDict['Greenland']=territory('Greenland', 'USA', 0)
  self.territoryDict['New Brunswick Nova Scotia']=territory('New Brunswick Nova Scotia', 'UK', 0)
  self.territoryDict['Newfoundland Labrador']=territory('Newfoundland Labrador', 'UK', 0)
  self.territoryDict['Central United States']=territory('Central United States', 'USA', 12)
  self.territoryDict['Eastern United States']=territory('Eastern United States', 'USA', 20)
  self.territoryDict['Southeast Mexico']=territory('Southeast Mexico', 'USA', 1)
  self.territoryDict['Central America']=territory('Central America', 'USA', 1)
  self.territoryDict['West Indies']=territory('West Indies', 'USA', 1)
  self.territoryDict['Colombia']=territory('Colombia', 'Colombia', 0)
  self.territoryDict['Venezuela']=territory('Venezuela','Venezuela',2)
  self.territoryDict['Ecuador']=territory('Ecuador','Ecuador',0)
  self.territoryDict['Peru']=territory('Peru', 'Peru', 0)
  self.territoryDict['Bolivia']=territory('Bolivia', 'Bolivia', 0)
  self.territoryDict['Paraguay']=territory('Paraguay', 'Paraguay', 0)
  self.territoryDict['Chile']=territory('Chile', 'Chile', 2)
  self.territoryDict['Argentina']=territory('Argentina', 'Argentina', 2)
  self.territoryDict['Uruguay']=territory('Uruguay', 'Uruguay', 0)
  self.territoryDict['Brazil']=territory('Brazil', 'Brazil', 2)
  self.territoryDict['Argentina']=territory('Argentina', 'Argentina', 2)
  self.territoryDict['French Guiana']=territory('French Guiana', 'France',0)
  self.territoryDict['Suriname']=territory('Suriname', 'Netherlands',0)
  self.territoryDict['British Guiana']=territory('British Guiana', 'UK',0)
  self.territoryDict['Iceland']=territory('Iceland', 'UK',0)
  self.territoryDict['Scotland']=territory('Scotland', 'UK',2)
  self.territoryDict['United Kingdom']=territory('United Kingdom', 'UK', 6)
  self.territoryDict['Eire']=territory('Eire', 'Eire', 0)
  self.territoryDict['Portuguese Guinea']=territory('Portuguese Guinea', 'UK', 0)
  self.territoryDict['French West Africa']=territory('French West Africa', 'France', 1)
  self.territoryDict['Sierra Leone']=territory('Sierra Leone', 'Sierra Leone', 0)
  self.territoryDict['Liberia']=territory('Liberia', 'Liberia', 0)
  self.territoryDict['Gold Coast']=territory('Gold Coast', 'UK', 0)
  self.territoryDict['Nigeria']=territory('Nigeria', 'UK', 1)
  self.territoryDict['French Equatorial Africa']=territory('French Equatorial Africa', 'France', 1)
  self.territoryDict['French Central Africa']=territory('French Central Africa', 'France', 1)
  self.territoryDict['Belgian Congo']=territory('Belgian Congo', 'UK', 1)
  self.territoryDict['Angola']=territory('Angola', 'Angola', 1)
  self.territoryDict['South West Africa']=territory('South West Africa', 'UK', 1)
  self.territoryDict['Union of South Africa']=territory('Union of South Africa','UK', 2)
  self.territoryDict['Rhodesia']=territory('Rhodesia', 'UK', 1)
  self.territoryDict['Kenya']=territory('Kenya', 'UK', 1)
  self.territoryDict['Mozambique']=territory('Mozambique', 'Mozambique', 1)
  self.territoryDict['French Madagascar']=territory('French Madagascar', 'France', 1)
  self.territoryDict['Tanganyika Territory']=territory('Tanganyika Territory', 'UK',1)
  self.territoryDict['Italian Somaliland']=territory('Italian Somaliland', 'Italy', 0)
  self.territoryDict['Ethiopia']=territory('Ethiopia', 'Italy', 1)
  self.territoryDict['British Somaliland']=territory('British Somaliland', 'UK', 0)
  self.territoryDict['Egypt']=territory('Egypt', 'UK', 2)
  self.territoryDict['Anglo-Egyptian Sudan']=territory('Anglo-Egyptian Sudan', 'UK', 1)
  self.territoryDict['Alexandria']=territory('Alexandria', 'UK', 0)
  self.territoryDict['Tobruk']=territory('Tobruk','Italy', 0)
  self.territoryDict['Libya']=territory('Lybia', 'Italy', 1)
  self.territoryDict['Tunisia']=territory('Tunisia', 'France', 1)
  self.territoryDict['Algeria']=territory('Algeria', 'France',1)
  self.territoryDict['Morocco']=territory('Morocco', 'France', 1)
  self.territoryDict['Rio de Oro']=territory('Rio de Oro','Rio de Oro',0)
  self.territoryDict['Gibraltar']=territory('Gibraltar','UK', 0)
  self.territoryDict['Spain']=territory('Spain', 'Spain',2)
  self.territoryDict['Portugal']=territory('Portugal', 'Portugal', 1)
  self.territoryDict['Normandy Bordeaux']=territory('Normandy Bordeaux','France',2)
  self.territoryDict['France']=territory('France','France', 4)
  self.territoryDict['Southern France']=territory('Southern France', 'France', 3)
  self.territoryDict['Holland Belgium']=territory('Holland Belgium','Germany', 3)
  self.territoryDict['Western Germany']=territory('Western Germany', 'Germany', 5)
  self.territoryDict['Denmark']=territory('Denmark', 'Germany', 2)
  self.territoryDict['Norway']=territory('Norway', 'Germany', 3)
  self.territoryDict['Sweden']=territory('Sweden', 'Sweden', 3)
  self.territoryDict['Finland']=territory('Finland', 'Finland', 2)
  self.territoryDict['Switzerland']=territory('Switzerland', 'Switzerland', 2)
  self.territoryDict['Northern Italy']=territory('Northern Italy', 'Italy', 4)
  self.territoryDict['Southern Italy']=territory('Southern Italy', 'Italy', 3)
  self.territoryDict['Sardinia']=territory('Sardinia', 'Italy', 0)
  self.territoryDict['Sicily']=territory('Sicily', 'Italy', 0)
  self.territoryDict['Malta']=territory('Malta', 'UK', 0)
  self.territoryDict['Germany']=territory('Germany', 'Germany', 5)
  self.territoryDict['Greater Southern Germany']=territory('Greater Southern Germany', 'Germany', 4)
  self.territoryDict['Poland']=territory('Poland', 'Germany', 2)
  self.territoryDict['Slovakia Hungary']=territory('Slovakia Hungary', 'Germany', 3)
  self.territoryDict['Romania']=territory('Romania', 'Romania', 3)
  self.territoryDict['Yugoslavia']=territory('Yugoslavia', 'Yugoslavia', 2)
  self.territoryDict['Albania']=territory('Albania', 'Italy', 1)
  self.territoryDict['Greece']=territory('Greece', 'Greece', 2)
  self.territoryDict['Crete']=territory('Crete', 'Crete', 0)
  self.territoryDict['Cyprus']=territory('Cyprus', 'UK', 0)
  self.territoryDict['Bulgaria']=territory('Bulgaria', 'Bulgaria', 1)
  self.territoryDict['Karelia']=territory('Karelia', 'USSR', 1)
  self.territoryDict['Vyborg']=territory('Vyborg', 'USSR', 0)
  self.territoryDict['Baltic States']=territory('Baltic States', 'USSR', 1)
  self.territoryDict['Belarus']=territory('Belarus', 'USSR', 1)
  self.territoryDict['Eastern Poland']=territory('Eastern Poland', 'USSR', 1)
  self.territoryDict['Western Ukraine']=territory('Western Ukraine', 'USSR', 2)
  self.territoryDict['Bessarabia']=territory('Bessarabia', 'USSR', 0)
  self.territoryDict['Novgorod']=territory('Novgorod', 'USSR', 2)
  self.territoryDict['Archangel']=territory('Archangel', 'USSR', 1)
  self.territoryDict['Smolensk']=territory('Smolensk', 'USSR', 1)
  self.territoryDict['Nenetsia']=territory('Nenetsia', 'USSR', 0)
  self.territoryDict['Urals']=territory('Urals', 'USSR', 1)
  self.territoryDict['Vologda']=territory('Vologda', 'USSR', 1)
  self.territoryDict['Novosibirsk']=territory('Novosibirsk', 'USSR', 1)
  self.territoryDict['Samara']=territory('Samara', 'USSR', 1)
  self.territoryDict['Tambov']=territory('Tambov','USSR',1)
  self.territoryDict['Russia']=territory('Russia', 'USSR', 3)
  self.territoryDict['Bryansk']=territory('Bryansk', 'USSR', 1)
  self.territoryDict['Ukraine']=territory('Ukraine', 'USSR', 2)
  self.territoryDict['Rostov']=territory('Rostov', 'USSR', 2)
  self.territoryDict['Caucasus']=territory('Caucasus', 'USSR', 2)
  self.territoryDict['Volgograd']=territory('Volgograd', 'USSR', 2)
  self.territoryDict['Kazakhstan']=territory('Kazakhstan', 'USSR', 1)
  self.territoryDict['Turkmenistan']=territory('Turkmenistan', 'USSR', 0)
  self.territoryDict['Afghanistan']=territory('Afghanistan', 'Afghanistan', 0)
  self.territoryDict['West India']=territory('West India', 'UK', 2)
  self.territoryDict['Eastern Persia']=territory('Eastern Persia', 'Eastern Persia', 0)
  self.territoryDict['Persia']=territory('Persia', 'Persia', 2)
  self.territoryDict['Northwest Persia']=territory('Northwest Persia', 'Northwest Persia', 0)
  self.territoryDict['Iraq']=territory('Iraq', 'Iraq', 2)
  self.territoryDict['Saudi Arabia']=territory('Saudi Arabia', 'Saudi Arabia', 2)
  self.territoryDict['Trans-Jordan']=territory('Trans-Jordan', 'UK', 1)
  self.territoryDict['Syria']=territory('Syria', 'France', 1)
  self.territoryDict['Turkey']=territory('Turkey', 'Turkey', 2)

  seaZoneNames=[]
  for i in range(64, 128):
   seaZoneNames.append('seaZone'+str(i))
  for x in seaZoneNames:
   seaZoneObj = territory(x,'Poseidon', 0)
   seaZoneObj.territoryType='Sea'
   self.territoryDict[x]=seaZoneObj
 
  self.constructBorder('Alberta Saskatchewan Manitoba','Ontario')
  self.constructBorder('Alberta Saskatchewan Manitoba','Central United States')
  self.constructBorder('Alberta Saskatchewan Manitoba','seaZone120')

  self.constructBorder('Ontario','Central United States')
  self.constructBorder('Ontario','Eastern United States')
  self.constructBorder('Ontario','Quebec')
  self.constructBorder('Ontario','seaZone120')
 
  self.constructBorder('Quebec','seaZone120')
  self.constructBorder('Quebec','seaZone121')
  self.constructBorder('Quebec','seaZone106')
  self.constructBorder('Quebec','Newfoundland Labrador')

  self.constructBorder('Newfoundland Labrador','seaZone116')
  self.constructBorder('New Brunswick Nova Scotia','Eastern United States')
  self.constructBorder('New Brunswick Nova Scotia', 'seaZone106')

  self.constructBorder('Central United States', 'Eastern United States')
  self.constructBorder('Central United States', 'Southeast Mexico')
  self.constructBorder('Central United States','seaZone101')

  self.constructBorder('Eastern United States', 'seaZone101')

  self.constructBorder('Southeast Mexico', 'Central America')
  self.constructBorder('Southeast Mexico', 'seaZone64')
  self.constructBorder('Southeast Mexico', 'seaZone89')

  self.constructBorder('Greenland','seaZone121')
  
  self.constructBorder('Central America','Colombia')
  self.constructBorder('Central America', 'seaZone64')
  self.constructBorder('Central America', 'seaZone89') 

  self.constructBorder('West Indies', 'seaZone89')

  self.constructBorder('Colombia', 'Ecuador')
  self.constructBorder('Colombia', 'Peru')
  self.constructBorder('Colombia','Venezuela')
  self.constructBorder('Colombia', 'Brazil')
  self.constructBorder('Colombia', 'seaZone64')
    
  self.constructBorder('Venezuela', 'Brazil')
  self.constructBorder('Venezuela', 'British Guiana')
  self.constructBorder('Venezuela', 'seaZone89')

  self.constructBorder('British Guiana', 'Suriname')
  self.constructBorder('British Guiana', 'Brazil')
  self.constructBorder('British Guiana', 'seaZone88')
  
  self.constructBorder('Suriname','Brazil')
  self.constructBorder('Suriname', 'French Guiana')
  self.constructBorder('Suriname', 'seaZone88') 

  self.constructBorder('French Guiana', 'Brazil')
  self.constructBorder('French Guiana', 'seaZone88')
  
  self.constructBorder('Brazil', 'Uruguay')
  self.constructBorder('Brazil', 'Argentina')
  self.constructBorder('Brazil', 'Paraguay')
  self.constructBorder('Brazil', 'Bolivia')
  self.constructBorder('Brazil', 'Peru')
  self.constructBorder('Brazil', 'seaZone86')
  self.constructBorder('Brazil', 'seaZone85')
 
  self.constructBorder('Uruguay', 'Argentina')
  self.constructBorder('Uruguay', 'seaZone88')

  self.constructBorder('Argentina', 'Paraguay')
  self.constructBorder('Argentina', 'Bolivia')
  self.constructBorder('Argentina', 'Chile')
  self.constructBorder('Argentina', 'seaZone66')

  self.constructBorder('Chile', 'Bolivia')
  self.constructBorder('Chile', 'seaZone66')
  self.constructBorder('Chile', 'seaZone65')
  self.constructBorder('Chile', 'Peru')

  self.constructBorder('Peru','seaZone65')
  self.constructBorder('Peru','Ecuador')

  self.constructBorder('Ecuador', 'seaZone64')

  self.constructBorder('Iceland', 'seaZone123')

  self.constructBorder('Eire', 'Scotland')
  self.constructBorder('Eire', 'seaZone119')
  self.constructBorder('Eire', 'seaZone109')

  self.constructBorder('Scotland','United Kingdom')
  self.constructBorder('Scotland', 'seaZone119')
  self.constructBorder('Scotland', 'seaZone109')
  self.constructBorder('Scotland', 'seaZone111')

  self.constructBorder('United Kingdom', 'seaZone109')
  self.constructBorder('United Kingdom', 'seaZone110')

  self.constructBorder('Portugal', 'seaZone91')
  self.constructBorder('Portugal', 'seaZone104')
  self.constructBorder('Portugal', 'Spain')

  self.constructBorder('Spain', 'Gibraltar')
  self.constructBorder('Spain', 'Normandy Bordeaux')
  self.constructBorder('Spain', 'Southern France')

  self.constructBorder('Spain', 'seaZone105')
  self.constructBorder('Spain', 'seaZone104')
  self.constructBorder('Spain', 'seaZone91')
  self.constructBorder('Spain', 'seaZone92')

  self.constructBorder('Normandy Bordeaux', 'seaZone110')
  self.constructBorder('Normandy Bordeaux', 'seaZone105')
  self.constructBorder('Normandy Bordeaux', 'France')
  self.constructBorder('Normandy Bordeaux', 'Southern France')
  self.constructBorder('Normandy Bordeaux', 'Holland Belgium')

  self.constructBorder('France','Holland Belgium')
  self.constructBorder('France', 'Western Germany')
  self.constructBorder('France', 'Switzerland')
  self.constructBorder('France','Southern France')
  self.constructBorder('France', 'Northern Italy')

  self.constructBorder('Southern France', 'Northern Italy')
  self.constructBorder('Southern France', 'seaZone93')

  self.constructBorder('Switzerland', 'Western Germany')
  self.constructBorder('Switzerland', 'Northern Italy')

  self.constructBorder('Northern Italy', 'Western Germany')
  self.constructBorder('Northern Italy', 'Greater Southern Germany')
  self.constructBorder('Northern Italy', 'Yugoslavia')
  self.constructBorder('Northern Italy', 'seaZone95')
  self.constructBorder('Northern Italy', 'seaZone97')
  self.constructBorder('Northern Italy', 'Southern Italy')

  self.constructBorder('Sardinia', 'seaZone95')
  self.constructBorder('Sicily','seaZone95')

  self.constructBorder('Southern Italy', 'seaZone95')
  self.constructBorder('Southern Italy', 'seaZone97')

  self.constructBorder('Holland Belgium', 'seaZone110')
  self.constructBorder('Holland Belgium', 'Western Germany')

  self.constructBorder('Western Germany','seaZone112')
  self.constructBorder('Western Germany','Denmark')
  self.constructBorder('Western Germany','seaZone113')
  self.constructBorder('Western Germany','Germany')
  self.constructBorder('Western Germany', 'Greater Southern Germany')

  self.constructBorder('Denmark','seaZone112')
  self.constructBorder('Denmark','seaZone113')

  self.constructBorder('Norway','seaZone113')
  self.constructBorder('Norway','seaZone112')
  self.constructBorder('Norway','seaZone125')
  self.constructBorder('Norway','seaZone126')
  self.constructBorder('Norway','Sweden')
  self.constructBorder('Norway', 'Finland')

  self.constructBorder('Sweden','seaZone113')
  self.constructBorder('Sweden','seaZone114')
  self.constructBorder('Sweden', 'seaZone115')
  self.constructBorder('Sweden', 'Finland')

  self.constructBorder('Finland', 'Karelia')
  self.constructBorder('Finland', 'Vyborg')
  self.constructBorder('Finland', 'seaZone115')

  self.constructBorder('Germany','seaZone113')
  self.constructBorder('Germany','seaZone114')
  self.constructBorder('Germany','Poland')
  self.constructBorder('Germany','Slovakia Hungary')
  self.constructBorder('Germany','Greater Southern Germany')

  self.constructBorder('Greater Southern Germany','Slovakia Hungary')
  self.constructBorder('Greater Southern Germany','Yugoslavia')

  self.constructBorder('Poland','seaZone114')
  self.constructBorder('Poland','Baltic States')
  self.constructBorder('Poland','Eastern Poland')
  self.constructBorder('Poland', 'Slovakia Hungary')

  self.constructBorder('Slovakia Hungary', 'Yugoslavia')
  self.constructBorder('Slovakia Hungary', 'Eastern Poland')
  self.constructBorder('Slovakia Hungary','Romania')

  self.constructBorder('Romania','Eastern Poland')
  self.constructBorder('Romania', 'Bessarabia')
  self.constructBorder('Romania', 'Bulgaria')
  self.constructBorder('Romania','Yugoslavia')

  self.constructBorder('Yugoslavia', 'seaZone97')
  self.constructBorder('Yugoslavia', 'Bulgaria')
  self.constructBorder('Yugoslavia', 'Albania')

  self.constructBorder('Albania','seaZone97')
  self.constructBorder('Albania','Greece')
  self.constructBorder('Albania', 'Bulgaria')

  self.constructBorder('Bulgaria','Greece')
  self.constructBorder('Bulgaria','seaZone100')

  self.constructBorder('Greece', 'seaZone97')
  self.constructBorder('Greece', 'seaZone99')
  self.constructBorder('Greece', 'Turkey')

  self.constructBorder('Crete','seaZone99')

  self.constructBorder('Cyprus','seaZone99')

  self.constructBorder('Karelia', 'seaZone127')
  self.constructBorder('Karelia','Vyborg')
  self.constructBorder('Karelia','Novgorod')

  self.constructBorder('Vyborg','Novgorod')
  self.constructBorder('Vyborg','seaZone115')

  self.constructBorder('Novgorod', 'seaZone127')
  self.constructBorder('Novgorod','Archangel')
  self.constructBorder('Novgorod','Belarus')
  self.constructBorder('Novgorod','Baltic States')
  self.constructBorder('Novgorod', 'seaZone115')

  self.constructBorder('Baltic States','seaZone115')
  self.constructBorder('Baltic States','Eastern Poland')
  self.constructBorder('Baltic States','Belarus')

  self.constructBorder('Eastern Poland','Belarus')
  self.constructBorder('Eastern Poland', 'Western Ukraine')
  self.constructBorder('Eastern Poland','Bessarabia')

  self.constructBorder('Western Ukraine', 'Bryansk')
  self.constructBorder('Western Ukraine','Ukraine')
  self.constructBorder('Western Ukraine','Bessarabia')

  self.constructBorder('Bessarabia','seaZone100')
  self.constructBorder('Bessarabia','Ukraine')

  self.constructBorder('Ukraine','seaZone100')
  self.constructBorder('Ukraine','Bryansk')
  self.constructBorder('Ukraine','Rostov')

  self.constructBorder('Belarus','Archangel')
  self.constructBorder('Belarus','Smolensk')
  self.constructBorder('Belarus','Bryansk')

  self.constructBorder('Archangel','seaZone127')
  self.constructBorder('Archangel', 'Nenetsia')
  self.constructBorder('Archangel','Vologda')
  self.constructBorder('Archangel','Smolensk')

  self.constructBorder('Nenetsia','seaZone127')
  self.constructBorder('Nenetsia','Urals')
  self.constructBorder('Nenetsia','Vologda')

  self.constructBorder('Urals','Vologda')
  self.constructBorder('Urals', 'Novosibirsk')

  self.constructBorder('Novosibirsk','Kazakhstan')
  self.constructBorder('Novosibirsk','Samara')
  self.constructBorder('Novosibirsk','Vologda')

  self.constructBorder('Vologda','Samara')
  self.constructBorder('Vologda','Russia')
  self.constructBorder('Vologda','Smolensk')

  self.constructBorder('Smolensk','Russia')
  self.constructBorder('Smolensk','Bryansk')

  self.constructBorder('Bryansk','Russia')
  self.constructBorder('Bryansk','Rostov')

  self.constructBorder('Rostov','seaZone100')
  self.constructBorder('Rostov','Caucasus')
  self.constructBorder('Rostov','Volgograd')
  self.constructBorder('Rostov','Tambov')

  self.constructBorder('Russia','Samara')
  self.constructBorder('Russia','Tambov')
  
  self.constructBorder('Tambov','Samara')
  self.constructBorder('Tambov','Volgograd')

  self.constructBorder('Samara','Kazakhstan')
  self.constructBorder('Samara','Volgograd')

  self.constructBorder('Volgograd','Kazakhstan')
  self.constructBorder('Volgograd','Caucasus')

  self.constructBorder('Caucasus','seaZone100')
  self.constructBorder('Caucasus','Turkey')
  self.constructBorder('Caucasus','Northwest Persia')

  self.constructBorder('Kazakhstan','Turkmenistan')
  self.constructBorder('Kazakhstan','Afghanistan')

  self.constructBorder('Turkmenistan','Afghanistan')
  self.constructBorder('Turkmenistan','Eastern Persia')

  self.constructBorder('Afghanistan','West India')
  self.constructBorder('Afghanistan','Eastern Persia')

  self.constructBorder('West India','seaZone79')
  self.constructBorder('West India','Eastern Persia')

  self.constructBorder('Eastern Persia','seaZone80')
  self.constructBorder('Eastern Persia','Persia')

  self.constructBorder('Persia','seaZone80')
  self.constructBorder('Persia','Northwest Persia')
  self.constructBorder('Persia','Iraq')

  self.constructBorder('Northwest Persia','Iraq')
  self.constructBorder('Northwest Persia','Turkey')

  self.constructBorder('Turkey','seaZone100')
  self.constructBorder('Turkey','Syria')
  self.constructBorder('Turkey','seaZone99')

  self.constructBorder('Syria','seaZone99')
  self.constructBorder('Syria','Iraq')
  self.constructBorder('Syria','Trans-Jordan')
  self.constructBorder('Syria','seaZone98')

  self.constructBorder('Iraq','seaZone80')
  self.constructBorder('Iraq','Saudi Arabia')
  self.constructBorder('Iraq','Trans-Jordan')

  self.constructBorder('Saudi Arabia','seaZone80')
  self.constructBorder('Saudi Arabia','seaZone76')
  self.constructBorder('Saudi Arabia','seaZone81')
  self.constructBorder('Saudi Arabia','Trans-Jordan')

  self.constructBorder('Trans-Jordan','seaZone98')
  self.constructBorder('Trans-Jordan','seaZone81')
  self.constructBorder('Trans-Jordan','Egypt')

  self.constructBorder('Egypt','seaZone98')
  self.constructBorder('Egypt','seaZone81')
  self.constructBorder('Egypt','Alexandria')

  self.constructBorder('Alexandria','seaZone98')
  self.constructBorder('Alexandria','Tobruk')

  self.constructBorder('Tobruk','seaZone96')
  self.constructBorder('Tobruk','Libya')

  self.constructBorder('Malta','seaZone96')
  self.constructBorder('Libya','seaZone96')
  self.constructBorder('Libya','Tunisia')

  self.constructBorder('Tunisia','seaZone94')
  self.constructBorder('Tunisia','Algeria')
  self.constructBorder('Algeria','seaZone94')
  self.constructBorder('Algeria','seaZone92')
  self.constructBorder('Algeria','Morocco')

  self.constructBorder('Morocco','seaZone92')
  self.constructBorder('Morocco','seaZone91')

  self.constructBorder('Gibraltar','seaZone92')
  self.constructBorder('Gibraltar','seaZone91')

  self.constructBorder('Egypt','Anglo-Egyptian Sudan')
  self.constructBorder('Anglo-Egyptian Sudan','Ethiopia')
  self.constructBorder('Anglo-Egyptian Sudan','seaZone81')
  self.constructBorder('Anglo-Egyptian Sudan','Kenya')
  self.constructBorder('Anglo-Egyptian Sudan','Belgian Congo')
  self.constructBorder('Anglo-Egyptian Sudan','French Equatorial Africa')

  self.constructBorder('French Equatorial Africa','French Central Africa')
  self.constructBorder('French Equatorial Africa','Nigeria')
  self.constructBorder('French Equatorial Africa','seaZone82')
  self.constructBorder('French Equatorial Africa','Belgian Congo')

  self.constructBorder('French Central Africa','Nigeria')
  self.constructBorder('French Central Africa','French West Africa')

  self.constructBorder('Nigeria','seaZone82')
  self.constructBorder('Nigeria','French West Africa')

  self.constructBorder('French West Africa','Gold Coast')
  self.constructBorder('French West Africa','seaZone82')
  self.constructBorder('French West Africa','seaZone83')
  self.constructBorder('French West Africa','seaZone87')
  self.constructBorder('French West Africa','Liberia')
  self.constructBorder('French West Africa','Sierra Leone')
  self.constructBorder('French West Africa','Portuguese Guinea')

  self.constructBorder('Gold Coast','seaZone82')

  self.constructBorder('Liberia','seaZone83')
  self.constructBorder('Sierra Leone','seaZone87')
  self.constructBorder('Liberia','Sierra Leone')

  self.constructBorder('Portuguese Guinea','seaZone87')

  self.constructBorder('Ethiopia','seaZone76')
  self.constructBorder('Ethiopia','British Somaliland')
  self.constructBorder('Ethiopia','Italian Somaliland')
  self.constructBorder('Ethiopia','Kenya')

  self.constructBorder('British Somaliland','seaZone76')
  self.constructBorder('British Somaliland','Italian Somaliland')
  self.constructBorder('Italian Somaliland','seaZone76')
  self.constructBorder('Italian Somaliland','Kenya')

  self.constructBorder('Kenya','seaZone72')
  self.constructBorder('Kenya','Tanganyika Territory')
  self.constructBorder('Kenya','Belgian Congo')

  self.constructBorder('Belgian Congo','Tanganyika Territory')
  self.constructBorder('Belgian Congo','seaZone70')
  self.constructBorder('Belgian Congo','Angola')
  self.constructBorder('Belgian Congo','Rhodesia')

  self.constructBorder('Angola','seaZone70')
  self.constructBorder('Angola','South West Africa')
  self.constructBorder('Angola','Rhodesia')

  self.constructBorder('Tanganyika Territory','seaZone72')
  self.constructBorder('Tanganyika Territory','Mozambique')
  self.constructBorder('Tanganyika Territory','Rhodesia')

  self.constructBorder('Mozambique','seaZone72')
  self.constructBorder('Mozambique','seaZone71')
  self.constructBorder('Mozambique','Rhodesia')
  self.constructBorder('Mozambique','Union of South Africa')

  self.constructBorder('Rhodesia','Union of South Africa')
  self.constructBorder('Rhodesia','South West Africa')

  self.constructBorder('Union of South Africa','seaZone71')
  self.constructBorder('South West Africa','seaZone70')

  self.constructBorder('French Madagascar','seaZone72')

  self.constructBorder('seaZone120','seaZone121')
  self.constructBorder('seaZone121','seaZone122')
  self.constructBorder('seaZone121','seaZone116')

  self.constructBorder('seaZone122','seaZone123')
  self.constructBorder('seaZone122','seaZone117')
  self.constructBorder('seaZone122','seaZone116')

  self.constructBorder('seaZone116','seaZone117')
  self.constructBorder('seaZone116','seaZone106')

  self.constructBorder('seaZone117','seaZone123')
  self.constructBorder('seaZone117','seaZone118')
  self.constructBorder('seaZone117','seaZone108')
  self.constructBorder('seaZone117','seaZone107')
  self.constructBorder('seaZone117','seaZone106')

  self.constructBorder('seaZone106','seaZone107')
  self.constructBorder('seaZone106','seaZone102')
  self.constructBorder('seaZone106','seaZone101')

  self.constructBorder('seaZone101','seaZone102')
  self.constructBorder('seaZone101','seaZone89')

  self.constructBorder('seaZone89','seaZone64')
  self.constructBorder('seaZone89','seaZone88')
  self.constructBorder('seaZone89','seaZone90')
  self.constructBorder('seaZone89','seaZone102')

  self.constructBorder('seaZone64','seaZone65')
  self.constructBorder('seaZone65','seaZone66')

  self.constructBorder('seaZone66','seaZone67')
  self.constructBorder('seaZone66','seaZone85')

  self.constructBorder('seaZone67','seaZone85')
  self.constructBorder('seaZone67','seaZone84')
  self.constructBorder('seaZone67','seaZone68')

  self.constructBorder('seaZone85','seaZone84')
  self.constructBorder('seaZone85','seaZone86')

  self.constructBorder('seaZone86','seaZone84')
  self.constructBorder('seaZone86','seaZone87')
  self.constructBorder('seaZone86','seaZone88')

  self.constructBorder('seaZone88','seaZone87')
  self.constructBorder('seaZone88','seaZone91')
  self.constructBorder('seaZone88','seaZone90')

  self.constructBorder('seaZone90','seaZone91')
  self.constructBorder('seaZone90','seaZone103')
  self.constructBorder('seaZone90','seaZone102')

  self.constructBorder('seaZone102','seaZone103')
  self.constructBorder('seaZone102','seaZone107')

  self.constructBorder('seaZone107','seaZone108')

  self.constructBorder('seaZone118','seaZone119')
  self.constructBorder('seaZone118','seaZone109')
  self.constructBorder('seaZone118','seaZone108')

  self.constructBorder('seaZone108','seaZone109')
  self.constructBorder('seaZone108','seaZone104')
  self.constructBorder('seaZone108','seaZone103')

  self.constructBorder('seaZone119','seaZone109')
  self.constructBorder('seaZone119','seaZone124')
  self.constructBorder('seaZone119','seaZone111')
  self.constructBorder('seaZone119','seaZone109')

  self.constructBorder('seaZone124','seaZone125')
  self.constructBorder('seaZone124','seaZone111')

  self.constructBorder('seaZone125','seaZone126')
  self.constructBorder('seaZone125','seaZone112')
  self.constructBorder('seaZone125','seaZone111')

  self.constructBorder('seaZone111','seaZone112')
  self.constructBorder('seaZone111','seaZone110')

  self.constructBorder('seaZone126','seaZone127')

  self.constructBorder('seaZone112','seaZone110')
  self.constructBorder('seaZone112','seaZone113')
  self.constructBorder('seaZone112','seaZone110')

  self.constructBorder('seaZone113','seaZone114')

  self.constructBorder('seaZone114','seaZone115')

  self.constructBorder('seaZone110','seaZone109')
  self.constructBorder('seaZone110','seaZone104')
  self.constructBorder('seaZone110','seaZone105')

  self.constructBorder('seaZone109','seaZone104')

  self.constructBorder('seaZone104','seaZone105')
  self.constructBorder('seaZone104','seaZone103')
  self.constructBorder('seaZone104','seaZone91')

  self.constructBorder('seaZone103','seaZone91')

  self.constructBorder('seaZone91','seaZone87')
  self.constructBorder('seaZone91','seaZone92')

  self.constructBorder('seaZone92','seaZone93')
  self.constructBorder('seaZone92','seaZone94')

  self.constructBorder('seaZone93','seaZone95')
  self.constructBorder('seaZone93','seaZone94')

  self.constructBorder('seaZone95','seaZone94')
  self.constructBorder('seaZone95','seaZone97')
  self.constructBorder('seaZone95','seaZone96')
  self.constructBorder('seaZone95','seaZone94')

  self.constructBorder('seaZone96','seaZone99')
  self.constructBorder('seaZone96','seaZone98')

  self.constructBorder('seaZone99','seaZone98')
  self.constructBorder('seaZone99','seaZone100')

  self.constructBorder('seaZone98','seaZone81')

  self.constructBorder('seaZone81','seaZone76')

  self.constructBorder('seaZone76','seaZone80')
  self.constructBorder('seaZone76','seaZone77')
  self.constructBorder('seaZone76','seaZone72')

  self.constructBorder('seaZone80','seaZone79')
  self.constructBorder('seaZone80','seaZone77')

  self.constructBorder('seaZone79','seaZone78')
  self.constructBorder('seaZone79','seaZone77')

  self.constructBorder('seaZone78','seaZone77')
  self.constructBorder('seaZone78','seaZone75')

  self.constructBorder('seaZone77','seaZone75')
  self.constructBorder('seaZone77','seaZone72')

  self.constructBorder('seaZone75','seaZone74')
  self.constructBorder('seaZone75','seaZone73')
  self.constructBorder('seaZone75','seaZone72')

  self.constructBorder('seaZone74','seaZone73')

  self.constructBorder('seaZone73','seaZone72')

  self.constructBorder('seaZone72','seaZone71')

  self.constructBorder('seaZone71','seaZone70')

  self.constructBorder('seaZone70','seaZone82')
  self.constructBorder('seaZone70','seaZone69')

  self.constructBorder('seaZone82','seaZone69')
  self.constructBorder('seaZone82','seaZone83')

  self.constructBorder('seaZone69','seaZone83')
  self.constructBorder('seaZone69','seaZone68')

  self.constructBorder('seaZone83','seaZone84')
  self.constructBorder('seaZone83','seaZone68')
  self.constructBorder('seaZone83','seaZone84')
  self.constructBorder('seaZone83','seaZone87')

  self.constructBorder('seaZone84','seaZone87')




 def initializePlayers(self):

  germany=nation('Germany')
  germany.stance = 'Axis'
  germany.IPC = 30
  germany.controlledTerritories=[]
  self.players[germany.name]=germany

  ussr=nation('USSR')
  ussr.stance = 'Neutral'
  ussr.IPC = 28
  ussr.controlledTerritories=[]
  self.players[ussr.name]=ussr
  

  uk=nation('UK')
  uk.stance = 'Allies'
  uk.IPC = 29
  uk.controlledTerritories=[]
  self.players[uk.name]=uk



  usa =nation('USA')
  usa.stance = 'Neutral'
  usa.IPC = 35
  usa.controlledTerritories=[]
  self.players[usa.name]=usa

  italy=nation('Italy')
  italy.stance='Axis'
  italy.IPC = 10
  italy.controlledTerritories=[]
  self.players[italy.name]=italy

  france=nation('France')
  france.stance='Allies'
  france.IPC = 17
  france.controlledTerritories=[]
  self.players[france.name]=france


  for territory in self.territoryDict:
   territoryObj=self.territoryDict[territory]
   for player in self.players:
    if territoryObj.originalOwner == player:
     territoryObj.currentOwner = player
     territoryObj.stance = self.players[player].stance
     self.players[player].controlledTerritories.append(territory)
   territoryObj.army=nullArmy
   territoryObj.army.location=territory
   territoryObj.army.owner=territoryObj.originalOwner


 def populateBoard(self):

  openingSetup={}  

  openingSetup['Germany']={'Infantry':11,'Artillery':3,'AAA':3,'Tactical Bomber':1,'Strategic Bomber':2, 'Major IC':1}
  openingSetup['Western Germany']={'Infantry':3,'Mech Infantry': 4, 'Artillery':1,'AAA': 3, 'Fighter': 2,'Tactical Bomber':3,'Air Base':1,'Naval Base':1, 'Major IC':1}
  openingSetup['Denmark']={'Infantry':2}
  openingSetup['Norway']={'Infantry':3,'Fighter':1}
  openingSetup['Holland Belgium']={'Infantry':4,'Artillery':2,'Tanks':3,'Fighter':1}
  openingSetup['Greater Southern Germany']={'Infantry':6,'Artillery':2,'Tanks':3}
  openingSetup['Slovakia Hungary']={'Infantry': 2,'Tank':1,'Fighter':1}
  openingSetup['Romania']={'Infantry':2,'Tank':1}
  openingSetup['Poland']={'Infantry':3,'Tank':1,'Tactical Bomber':1}
  openingSetup['seaZone103']={'Submarine':1}
  openingSetup['seaZone108']={'Submarine':1}
  openingSetup['seaZone118']={'Submarine':1}
  openingSetup['seaZone117']={'Submarine':1}
  openingSetup['seaZone124']={'Submarine':1}
  openingSetup['seaZone113']={'Battleship':3}
  openingSetup['seaZone114']={'Transport':1,'Cruiser':1}


  openingSetup['Southern Italy']={'Infantry':6,'AAA':2,'Fighter':2,'Air Base':1,'Naval Base':1,'Minor IC':1}
  openingSetup['Northern Italy']={'Infantry':2,'Artillery':2,'Tank':1,'AAA':2,'Strategic Bomber':1,'Major IC':1}
  openingSetup['Albania']={'Infantry':2,'Tank':1}
  openingSetup['Libya']={'Infantry':1,'Artillery':1}
  openingSetup['Tobruk']={'Infantry':3,'Artillery':1,'Mech Infantry':1,'Tank':1}
  openingSetup['Italian Somaliland']={'Infantry':1}
  openingSetup['Ethiopia']={'Infantry':2,'Artillery':1}
  openingSetup['seaZone95']={'Transport':1,'Submarine':1,'Destroyer':1,'Cruiser':1}
  openingSetup['seaZone96']={'Transport':1,'Destroyer':1}
  openingSetup['seaZone97']={'Transport':1,'Battleship':1,'Cruiser':1}



  for territoryName in openingSetup:
   territoryObj=self.territoryDict[territoryName]
   if (territoryObj.originalOwner != 'Poseidon'):
    startingArmy = army(territoryName, controller=territoryObj.originalOwner)
    for key in openingSetup[territoryName]:
     if (key in unitStats):
      startingArmy.addUnit(key,n=openingSetup[territoryName][key])
     elif (key in installation_types):
      territoryObj.addInstallation(key)
    territoryObj.addArmy(territoryObj.originalOwner, startingArmy)



 def buildTheaters(self):


  westernEuropeZones = {}
  middleEastZones={}
  africaZones ={}
  easternEuropeZones={}
  southEastAsiaZones={}
  atlanticZones={}
  siberiaZones={}

  greatBritainTerritories = self.territoryDict['United Kingdom'].borders + ['United Kingdom','seaZone111','seaZone119','Eire','seaZone118','seaZone123','Iceland']
  greatBritainZone = zoneOfControl('Great Britain', greatBritainTerritories, self.territoryDict)
  westernEuropeZones['Great Britain']=greatBritainZone
  
  franceTerritories = ['France', 'Holland Belgium', 'Normandy Bordeaux','Southern France','seaZone105','seaZone93']
  westernEuropeZones['France']=zoneOfControl('France', franceTerritories,self.territoryDict)

  iberiaTerritories = self.territoryDict['Portugal'].borders + ['Portugal','Gibraltar']
  westernEuropeZones['Iberia'] = zoneOfControl('Iberia',iberiaTerritories, self.territoryDict)

  northAfricaTerritories =self.territoryDict['Algeria'].borders +['Algeria']
  westernEuropeZones['North Africa']=zoneOfControl('North Africa',northAfricaTerritories, self.territoryDict)

  egyptTerritories = self.territoryDict['Egypt'].borders + ['Egypt','seaZone96','Malta','Lybia','Tobruk']
  middleEastZones['Egypt']=zoneOfControl('Egypt',egyptTerritories, self.territoryDict)

  persiaTerritories = self.territoryDict['Persia'].borders +['Saudi Arabia','Persia','seaZone77','Afghanistan','Syria']
  middleEastZones['Persia']=zoneOfControl('Persia',persiaTerritories, self.territoryDict)

  caucasusTerritories = ['Caucasus','Rostov','Volgograd','Kazakhstan','Turkmenistan']
  easternEuropeZones['Caucasus']=zoneOfControl('Caucasus',caucasusTerritories, self.territoryDict)
  
  ukraineTerritories =['Bessarabia','Western Ukraine','Ukraine','seaZone100']
  easternEuropeZones['Ukraine']=zoneOfControl('Ukraine',ukraineTerritories, self.territoryDict)
  
  russiaTerritories=self.territoryDict['Russia'].borders +['Russia']
  easternEuropeZones['Russia']=zoneOfControl('Russia',russiaTerritories, self.territoryDict)
  
  siberiaZones['Central Asia']=zoneOfControl('Central Asia',['Urals','Novosibirsk'], self.territoryDict)

  novgorodTerritories = self.territoryDict['Novgorod'].borders+['Novgorod','Nenetsia']
  easternEuropeZones['Novgorod']=zoneOfControl('Novgorod',novgorodTerritories, self.territoryDict)
  
  scandanaviaTerritories =['seaZone125','seaZone126','Norway','Sweden','Finland']
  westernEuropeZones['Scandanavia']=zoneOfControl('Scandanavia',scandanaviaTerritories, self.territoryDict)

  polandTerritories=['seaZone114','Poland','Slovakia Hungary','Romania','Eastern Poland']
  easternEuropeZones['Poland']=zoneOfControl('Poland',polandTerritories, self.territoryDict)
  
  germanyTerritories = ['Western Germany','Denmark','seaZone112','seaZone113','Germany','Greater Southern Germany']
  westernEuropeZones['Germany'] = zoneOfControl('Germany',germanyTerritories, self.territoryDict)

  
  italyTerritories=['Northern Italy','Switzerland','Southern Italy','seaZone97','seaZone95','Sardinia','Sicily']
  westernEuropeZones['Italy'] = zoneOfControl('Italy',italyTerritories, self.territoryDict)

  balkanTerritories = ['Yugoslavia','Bulgaria','Albania','Greece','seaZone99','Crete','Cyprus','Turkey']
  easternEuropeZones['Balkans'] = zoneOfControl('Balkans',balkanTerritories, self.territoryDict)


  centralAtlanticTerritories =['seaZone117','seaZone107','seaZone108','seaZone103','seaZone102','seaZone90']
  atlanticZones['Central Atlantic']=zoneOfControl('Central Atlantic',centralAtlanticTerritories, self.territoryDict)

  canadaTerritories =self.territoryDict['seaZone120'].borders + ['seaZone120','New Brunswick Nova Scotia','seaZone106','seaZone116','seaZone121','seaZone122']
  atlanticZones['Canada']=zoneOfControl('Canada',canadaTerritories, self.territoryDict)


  easternUSTerritories = ['Central United States','Eastern United States','seaZone 101']
  atlanticZones['Eastern United States']=zoneOfControl('Eastern United States', easternUSTerritories, self.territoryDict)


  centralAmericaTerritories =['Southeast Mexico','seaZone89','West Indies','Central America','seaZone64']
  atlanticZones['Central America']=zoneOfControl('Central America',centralAmericaTerritories, self.territoryDict)


  southAmericaTerritories = self.territoryDict['Peru'].borders +self.territoryDict['Argentina'].borders + ['Peru','Argentina','seaZone88','British Guiana','Suriname','French Guiana','seaZone86','seaZone67','seaZone84','seaZone68']
  atlanticZones['South America']=zoneOfControl('South America',southAmericaTerritories, self.territoryDict)
  

  self.theaters={'Western Europe':theater('Western Europe', westernEuropeZones, self.territoryDict),'Middle East':theater('MiddleEast',middleEastZones, self.territoryDict),'Africa':theater('Africa',africaZones, self.territoryDict),'Eastern Europe':theater('Eastern Europe', easternEuropeZones, self.territoryDict),'Atlantic':theater('Atlantic',atlanticZones, self.territoryDict),'Siberia':theater('Siberia',siberiaZones, self.territoryDict)}
  


  
  


 def __init__(self):
  self.territoryDict={}
  self.buildMap()
  self.initializePlayers()
  self.populateBoard()
  self.buildTheaters()  




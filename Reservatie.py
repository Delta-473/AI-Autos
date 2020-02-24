	# reservatie
		# id String
		# dag int
		# zone-id String
		# start int
		# duur int
		# voertuigen[] Strings
		# pentalty1 int
		# pentalty2 int
from typing import List
from AI-Autos.Zone import Zone

class Reservatie 		
	def __init__(self, id, zone, dag, start, duur, voertuigen, penalty1, penalty2,)
		self.id = str(id)
		self.zone= Zone(zone)
		self.dag = int(dag)
		self.start= int(start)
		self.duur= int(duur)
		self.voertuigen= List[str]=voertuigen.split(",") 
		self.penalty1=int(penalty1
		self.penalty2= int(penalty2)
	


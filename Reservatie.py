<<<<<<< HEAD
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
	
=======
class Reservatie():
    resId=""
    zoneId=""
    dag=0
    start=0
    duur=0
    voertuigen=""
    pentalty1=0
    pentalty2=0

    def __init__(self, resId, zoneId, dag,  start, duur, voertuigen, p1,p2):
        self.resId=resId
        self.zoneid=zoneId
        self.dag=dag
        self.start=start
        self.duur=duur
        self.voertuigen=voertuigen
        self.pentalty1=p1
        self.pentalty2=p2
       
    def  __str__(self):
        print("resId",self.resId)
        print("zoneid",self.zoneId)
        print("dag",self.dag)
        print("start",self.start)
        print("duur",self.duur)
        print("voertuigen",self.voertuigen)
        print("pentalty1",self.pentalty1)
        print("pentalty2",self.pentalty2)

>>>>>>> origin/master


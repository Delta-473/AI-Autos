
<<<<<<< HEAD
class Zone():
    zoneId=""
    neighbours=""

    def _init_(self, zoneId, neighbours):
        self.zoneId= zoneId
        self.neighbours = neighbours
       
    def __str__(self):
        print('Zone <id: '+self.zoneId+', neighbours: '+(self.neighbours)+'')
=======
from typing import Set
class Zone:
	def _init_(self, id, neighbours):
		self.id= id
        self.neighbours: Set[str] = set(neighbours.split(","))	# To intialize a set with values, you can pass in a list to set()
		
	def __str__(self):
        return 'Zone <id: '+self.id+', neighbours: '+(self.neighbours)+''
>>>>>>> fe742b9a21af34c7456dc9d8863609e5c9865172
		
	
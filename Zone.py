#	Zone
#		id String
#		zone aanliggende [] Strings


class Zone:
	def _init_(self, id, neighbours):
		self.id= id
        self.neighbours: [str] = set(neighbours.split(","))	# To intialize a set with values, you can pass in a list to set()
		
	def __str__(self):
        return 'Zone <id: '+self.id+', neighbours: '+(self.neighbours)+''
		
	
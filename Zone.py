
class Zone():
    zoneId=""
    neighbours=""

    def _init_(self, zoneId, neighbours):
        self.zoneId= zoneId
        self.neighbours = neighbours
       
    def __str__(self):
        print('Zone <id: '+self.zoneId+', neighbours: '+(self.neighbours)+'')
		
	


class Zone():
    zoneId=""
    neighbours=""

    def __init__(self, zoneId, neighbours):
        self.zoneId= zoneId
        self.neighbours = neighbours

    def __str__(self):
        return 'ZoneID: ' + self.zoneId + ', neighbours: ' + self.neighbours + ''

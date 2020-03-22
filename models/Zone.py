

class Zone():
    zoneId=""
    neighbours=""

    def __init__(self, zoneId, neighbours):
        self.zoneId= zoneId
        self.neighbours = neighbours

    def getName(self):
        return self.zoneId

    def getZones(self):
        return self.neighbours

    def __str__(self):
        return f"ZoneID: {self.zoneId}, neighbours: {self.neighbours}"



class Zone():
    zoneID=""
    neighbours=[] #strings van buren zoneId

    def __init__(self, zoneId, neighbours):
        self.zoneId= zoneId
        self.neighbours = neighbours

    def getName(self):
        return self.zoneID

    def getZones(self):
        return self.neighbours

    def __str__(self):
        string=""
        for buur in self.neighbours:
            string.append(buur)
            string.append(',')
        return f"ZoneID: {self.zoneId}, neighbours: {string}"

    def getZoneID(self):
        return self.zoneID

    def isBuur(self, buur):
        for b in self.neighbours:
            if (buur == b):
                return True
        return False



class Zone():
    zoneId=""
    neighbours[] #strings van buren zoneId

    def __init__(self, zoneId, neighbours):
        self.zoneId= zoneId
        self.neighbours = neighbours

    def getName(self):
        return self.name

    def getZones(self):
        return self.zones

    def __str__(self):
        string=""
        for buur in neighbours:
            string.append(buur)
            string.append(',')
        return f"ZoneID: {self.zoneId}, neighbours: {string}"

    def getZoneId(self):
        return self.zoneID

    def isBuur(self, buur):
        for b in neighbours:
            if (buur == b):
                return True
        return False

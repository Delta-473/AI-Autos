class Zone():
    zoneID=""
    neighbours=[] #strings van buren zoneID

    def __init__(self, zoneID, neighbours):
        self.zoneID= zoneID
        self.neighbours = neighbours

    def getZones(self):
        return self.neighbours

    def __str__(self):
        string=""
        for buur in self.neighbours:
            string+=f"{buur}"
            string+=','
        return f"{self.zoneID};{string}"

    def getZoneID(self):
        return self.zoneID

    def isBuur(self, buur):
        for b in self.neighbours:
            if (buur == b):
                return True
        return False

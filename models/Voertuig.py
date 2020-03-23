from models import data


class Voertuig():
    id=""
    zoneId=""

    def __init__(self,id):
        self.id=id
        #print("voertuig made",self.id)

    #def getID(self):
     #   return self.id

    def __str__(self):
        return f"Voertuig ID: {self.id} en zone ID: {self.zoneId}"

    def getZone(self):
        return self.zoneID

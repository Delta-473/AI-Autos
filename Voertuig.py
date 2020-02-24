import data;
class 	Voertuig(data):
    id=""
    zoneId=""
    def __init__(self,id):
        self.id=id
        print("voertuig made",self.id)

    def print(self):
        print("Voertuig ID: %s en zone ID: %s" % (self.id, self.zoneId))
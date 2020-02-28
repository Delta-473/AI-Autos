from models import data


class Voertuig():
    id=""
    zoneId=""
    def __init__(self,id):
        self.id=id
        print("voertuig made",self.id)

    def __str__(self):
        print("Voertuig ID: %s en zone ID: %s" % (self.id, self.zoneId))
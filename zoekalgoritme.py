import time
import random

from models.Reservatie import Reservatie
from models.Zone import Zone
from models.Voertuig import Voertuig

class zoekalgoritme():

    voertuig_zone = []
    temp_voertuig_zone = []
    kost = 0

    def init_oplossing(self, reservaties, voertuigen, zones):
        self.aantal_reservaties = len(reservaties)
        self.aantal_voertuigen = len(voertuigen)
        self.aantal_zones = len(zones)

        for res in reservaties:
            for i in (0, len(res.getVoertuigen)):
                if(not(res.checkVoertuigToegewezen(i))):#nog niet toegewezen
                    res.setVoertuigToegewezen(i)        #zelf toewijzen
                    resZone=res.getZone()

                    #tegen het voertuig zeggen dat die toegewezen is, eerst voertuig vinden
                    voertuigTeZoeken=res.getVoertuigIndex(i)
                    for voertuig in (voertuigen):
                        if(voertuig.getID==voertuigTeZoeken):
                            break
                    voertuig.setZoneID(resZone)

            #check of zijn reservatie is nu volledig compleet is
            res.selfCheck()


    def __init__(self, reservaties, voertuigen, zones):
        self.aantal_reservaties = len(reservaties)
        self.aantal_voertuigen = len(voertuigen)
        self.aantal_zones = len(zones)
        i = 0
        for voertuig in voertuigen:
            voertuig.zoneId = f"z{random.randint(0, self.aantal_zones)}"

        #while i < self.aantal_voertuigen:
        self.voertuig_zone = voertuigen
        self.temp_voertuig_zone = self.voertuig_zone
        self.kost = self.bereken_kost(reservaties, self.voertuig_zone)

    def reservaties_toewijzen(self, reservaties):
        for reservatie in reservaties:
            for voertuig in self.temp_voertuig_zone:
                if reservatie.zoneId == voertuig.zoneId:
                    if voertuig.id in reservatie.voertuigen:
                        reservatie.voertuigId = voertuig.id
                        reservatie.toegewezen = True


    def zoek(self, tijd, reservaties, voertuigen):

        print(f"#reservaties {self.aantal_reservaties} #voertuigen {self.aantal_voertuigen} #zones {self.aantal_zones}")

        while time.time() < tijd:
            #reservaties toewijzen
            self.reservaties_toewijzen(reservaties)

            #wijzig random voertuig toe aan random zone
            self.temp_voertuig_zone[random.randint(0, self.aantal_voertuigen - 1)].zoneId = f"z{random.randint(0, self.aantal_zones - 1)}"

            # bereken kost
            nieuwe_kost = self.bereken_kost(reservaties, self.temp_voertuig_zone)

            if self.kost > nieuwe_kost:
                self.voertuig_zone = self.temp_voertuig_zone
                self.kost = nieuwe_kost
            else:
                self.temp_voertuig_zone = self.voertuig_zone

        return self.kost

    def bereken_kost(self, reservaties, voertuigen):
        som=0
        for res in reservaties:
            if res.isToegewezen():
                for voertuig in voertuigen:
                    if not(res.zoneId == voertuig.zoneId):
                        som += int(res.getp2(), base=10)
                        break
            else:
                som += int(res.getp1(), base=10)

        return som

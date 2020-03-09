from random import random

from models.Reservatie import Reservatie
from models.Zone import Zone
from models.Voertuig import Voertuig

class zoekalgoritme():

    voertuig_zone = []
    temp_voertuig_zone = []
    kost = 0

    def __init__(self, reservaties, voertuigen, zones):
        self.aantal_reservaties = len(reservaties)
        self.aantal_voertuigen = len(voertuigen)
        self.aantal_zones = len(zones)
        i = 0
        while i < self.aantal_voertuigen:
            self.voertuig_zone.append("z" + random.randint(0, self.aantal_zones))
        self.temp_voertuig_zone = self.voertuig_zone
        kost = 0 #ToDo: kostenfunctie

    def zoek(self, pogingen):

        print(f"#reservaties {self.aantal_reservaties} #voertuigen {self.aantal_voertuigen} #zones {self.aantal_zones}")

        i = 0
        while i < pogingen:
            self.temp_voertuig_zone[random.randint(0, self.aantal_voertuigen)] = "z" + random.randint(0, self.aantal_zones)

            # bereken kost
            nieuwe_kost = 0 #ToDo: kostenfunctie

            if self.kost > nieuwe_kost:
                self.voertuig_zone = self.temp_voertuig_zone
                self.kost = nieuwe_kost
            else:
                self.temp_voertuig_zone = self.voertuig_zone

            i += 1

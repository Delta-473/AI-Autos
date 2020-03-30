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

        for res in reservaties:
            for index in (0, len(res.getVoertuigen())):
                voertuig = self.returnVoertuigFromIndex(voertuigen, res,index)  # auto object vinden met behulp van index
                zoneId = self.checkVoertuigToegewezen(voertuig)
                if not (zoneId):  # controleert of er al iet in string zit
                    # nog niet toegewezen
                    if voertuig.kanWordenToegevoegdReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur()):

                        res.setVoertuigToegewezen(index)  # zelf toewijzen door de vlag op true te zetten
                        resZone = res.getZone()

                        # tegen het voertuig zeggen dat die toegewezen is
                        voertuig.setZoneID(resZone)
                        voertuig.AddReservatie(self, res.getDag(), res.getStart(), res.getStart() + res.getDuur(), res.getResId())

                        # check of zijn reservatie is nu volledig compleet is
                        self.reservatieCheck(res)
                else:  # voertuig is ergens anders al TOEGEWEZEN
                    res.setVoertuigNietToegewezen(index)

    def reservatieCheck(self, reservatie, voertuigen, zones):
        # controleert of reservatie volledig is (true als alle auto's zijn toegewezen aan zichzelf of aan buren)
        # false als een auto niet toegewezen is aan reservatie of zijn buur
        teller = 0
        for autoTrueOrFalse in reservatie.getVoertuigFlag():  # return bit array met indicatie of auto is toegewezen
            if autoTrueOrFalse:
                # auto is aan deze zone TOEGEWEZEN
                continue
            else:
                # auto is niet aan deze reservatie toegewezen, maar misschien wel aan een buur
                voertuig = self.returnVoertuigFromIndex(voertuigen, reservatie, teller)
                zoneId = voertuig.getZone()
                zone = self.returnZoneFromZoneId(zones, zoneId)
                if zone.isBuur(reservatie.getZone()):
                    # auto is aan buur toegewezen dus reservatie is voorlopig nog Compleet
                    continue
                else:
                    # niet bij de buur en ook niet bij zichzelf
                    reservatie.setReservatieToegewezen(False)
                    return

            teller += 1

    def checkVoertuigToegewezen(self, voertuig):
        zoneId = voertuig.getZone()
        return zoneId

    def returnZoneFromZoneId(self, zones, zone):
        for z in zones:
            if z.getZoneId() == zone:
                return z
        print("er is iets kapot ik heb een zone moeten zoeken met deze naam:", str(zone))

    def returnVoertuigFromIndex(self, voertuigen, reservatie, voertuigIndex):
        # we hebben de indexerende bit en de reservatie
        # return ons nu het voertuig
        voertuigTeZoeken = reservatie.getVoertuigIndex(voertuigIndex)
        for voertuig in voertuigen:
            if voertuig.getID() == voertuigTeZoeken:
                return voertuig
            print("er is iets kapot ik heb een voertuig moeten zoeken met deze naam:",voertuigTeZoeken)

    def __init__(self, reservaties, voertuigen, zones):
        self.aantal_reservaties = len(reservaties)
        self.aantal_voertuigen = len(voertuigen)
        self.aantal_zones = len(zones)

        self.init_oplossing(reservaties, voertuigen, zones)

        '''i = 0
        for voertuig in voertuigen:
            voertuig.zoneId = f"z{random.randint(0, self.aantal_zones)}"

        # while i < self.aantal_voertuigen:
        self.voertuig_zone = voertuigen
        self.temp_voertuig_zone = self.voertuig_zone
        self.kost = self.bereken_kost(reservaties, self.voertuig_zone)'''

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
            # reservaties toewijzen
            self.reservaties_toewijzen(reservaties)

            # wijzig random voertuig toe aan random zone
            self.temp_voertuig_zone[
                random.randint(0, self.aantal_voertuigen - 1)].zoneId = f"z{random.randint(0, self.aantal_zones - 1)}"

            # bereken kost
            nieuwe_kost = self.bereken_kost(reservaties, self.temp_voertuig_zone)

            if self.kost > nieuwe_kost:
                self.voertuig_zone = self.temp_voertuig_zone
                self.kost = nieuwe_kost
            else:
                self.temp_voertuig_zone = self.voertuig_zone

        return self.kost

    def bereken_kost(self, reservaties, voertuigen):
        som = 0
        for res in reservaties:
            if res.isToegewezen():
                for voertuig in voertuigen:
                    if not (res.zoneId == voertuig.zoneId):
                        som += int(res.getp2(), base=10)
                        break
            else:
                som += int(res.getp1(), base=10)

        return som

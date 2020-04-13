import time
import random
import copy
import math

from models.Reservatie import Reservatie
from models.Zone import Zone
from models.Voertuig import Voertuig


class zoekalgoritme():
    voertuig_zone = []
    temp_voertuig_zone = []

    save_voertuig_zone = copy.deepcopy(voertuig_zone)
    save_temp_voertuig_zone = copy.deepcopy(temp_voertuig_zone)
    save_kost = 0

    def nieuwe_init_oplossing(self, reservaties, voertuigen, zones):
        for auto in voertuigen:
            auto.setZoneID(zones[random.randint(0, self.aantal_zones - 1)].getZoneID())

    def init_oplossing(self, reservaties, voertuigen, zones):

        for res in reservaties:
            for resBuur in reservaties:
                zoneZelf = self.returnZoneFromZoneId(zones, res.getZone())
                zoneBuur = self.returnZoneFromZoneId(zones, resBuur.getZone())
                if zoneBuur.isBuur(zoneZelf):
                    voertuig = self.returnVoertuigFromString(voertuigen, resBuur.getToegewezenVoertuig())
                    for v in res.getVoertuigen():
                        if voertuig.getID() == v:
                            if voertuig.kanWordenToegevoegdReservatie(res.getDag(), res.getStart(),res.getStart() + res.getDuur(), res.getResID()):
                                voertuig.AddReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(), res.getResID())
                                res.setToegewezenVoertuig(voertuigNaam)  # zelf toewijzen, door de false
                                resZone = res.getZone()

                                # tegen het voertuig zeggen dat die toegewezen is
                                voertuig.setZoneID(resZone)


            for voertuigNaam in res.getVoertuigen():
                voertuig = self.returnVoertuigFromString(voertuigen, voertuigNaam)  # auto object vinden
                zoneID = voertuig.getZone()

                if not (zoneID):  # controleert of er al iet in string zit
                    # nog niet toegewezen
                    if voertuig.kanWordenToegevoegdReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(), res.getResID()):

                        res.setToegewezenVoertuig(voertuigNaam)  # zelf toewijzen door de vlag op true te zetten
                        resZone = res.getZone()

                        # tegen het voertuig zeggen dat die toegewezen is
                        voertuig.setZoneID(resZone)
                        voertuig.AddReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(), res.getResID())

                else:  # voertuig is ergens anders al TOEGEWEZEN
                    pass

        for res in reservaties:
            # check of zijn reservatie is nu compleet zijn of niet
            self.reservatieCheck(res, voertuigen, zones)

    def reservatieCheck(self, reservatie, voertuigen, zones):
        # controleert of reservatie volledig is (true als een auto is toegewezen aan zichzelf of aan buren)
        # false als een auto niet toegewezen is aan reservatie of zijn buur
        if reservatie.getToegewezenVoertuig():
            reservatie.setReservatieToegewezen(True)
        else:
            # auto is niet aan deze reservatie toegewezen, maar misschien wel aan een buur
            for auto in reservatie.getVoertuigen():
                voertuig = self.returnVoertuigFromString(voertuigen, auto)
                zoneID = voertuig.getZone()
                zone = self.returnZoneFromZoneId(zones, zoneID)
                if zone.isBuur(reservatie.getZone()):
                    # auto is aan buur toegewezen dus reservatie is Compleet
                    reservatie.setReservatieToegewezen(True)

                    break
                continue
            else:
                pass
               # niet bij de buur en ook niet bij zichzelf

        teller = 0
        for autoTrueOrFalse in reservatie.getVoertuigFlag():  # return bit array met indicatie of auto is toegewezen
            if autoTrueOrFalse:
                # auto is aan deze zone TOEGEWEZEN
                continue
            else:
                # auto is niet aan deze reservatie toegewezen, maar misschien wel aan een buur
                voertuig = self.returnVoertuigFromIndex(voertuigen, reservatie, teller)
                zoneID = voertuig.getZone()
                zone = self.returnZoneFromZoneId(zones, zoneID)
                if zone.isBuur(reservatie.getZone()):
                    # auto is aan buur toegewezen dus reservatie is voorlopig nog Compleet

                    continue
                else:
                    # niet bij de buur en ook niet bij zichzelf
                    reservatie.setReservatieToegewezen(False)
                    return
            teller += 1
        reservatie.setReservatieToegewezen(True)


    def returnZoneFromZoneId(self, zones, zone):#geeft het Zone object terug van een gegeven string
        for z in zones:
            if z.getZoneID() == zone:
                return z
        print("er is iets kapot ik heb een zone moeten zoeken met deze naam:", zone)

    def returnVoertuigFromString(self, voertuigen, voertuigTeZoeken):
        for voertuig in voertuigen:
            if voertuig.getID() == voertuigTeZoeken:
                return voertuig
        print("er is iets kapot ik heb een voertuig moeten zoeken met deze naam:",voertuigTeZoeken)

    def __init__(self, reservaties, voertuigen, zones):
        self.aantal_reservaties = len(reservaties)
        self.aantal_voertuigen = len(voertuigen)
        self.aantal_zones = len(zones)

        self.nieuwe_init_oplossing(reservaties, voertuigen, zones)

        for voertuig in voertuigen:
            voertuig.setZoneID(f"z{random.randint(0, self.aantal_zones - 1)}")

        self.voertuig_zone = voertuigen
        self.temp_voertuig_zone = self.voertuig_zone
        self.save_kost = self.bereken_kost(reservaties, self.voertuig_zone)

############################################################################################

    def reservaties_toewijzen(self, reservaties, zones):
        for res in reservaties:
            zoneID = int(res.zoneID[1:])
            naburigeZones = zones[zoneID].getZones()
            oplossingBuur = []
            oplossingGevondenInZone = False
            for voertuig in self.temp_voertuig_zone:
                #Voertuig ligt in dezelfde zone als request => beste oplossing
                if res.zoneID == voertuig.zoneID:
                    if voertuig.ID in res.voertuigen:
                        if voertuig.kanWordenToegevoegdReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(), res.getResID()):
                            voertuig.AddReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(),res.getResID())
                            res.voertuigID = voertuig.ID
                            res.toegewezen = True
                            oplossingGevondenInZone = True
                            break
                else:
                    for buren in naburigeZones:
                        #Voertuig ligt in naburige zone => tijdelijk opslaan en zoeken naar voertuig dat wel in dezelfde zone ligt
                        if buren == voertuig.zoneID:
                            if voertuig.kanWordenToegevoegdReservatie(res.getDag(), res.getStart(),res.getStart() + res.getDuur(), res.getResID()):
                                oplossingBuur.append(res.getDag())
                                oplossingBuur.append(res.getStart())
                                oplossingBuur.append(res.getStart() + res.getDuur())
                                oplossingBuur.append(res.getResID())
                                oplossingBuur.append(voertuig.ID)
                                break
            #Geen voertuig gevonden in dezelfde zone, neem dan oplossing van naburige zone als die er is
            if oplossingGevondenInZone == False and len(oplossingBuur) != 0:
                voertuig.AddReservatie(oplossingBuur[0], oplossingBuur[1], oplossingBuur[2], oplossingBuur[3])
                res.voertuigID = oplossingBuur[4]
                res.toegewezen = True

    def valideerReservaties(self, reservaties, voertuigen, zones):
    #ToDo: efficienter maken
        for res in reservaties:
            if res.isToegewezen(): #reservatie is toegewezen
                res_voer = res.getToegewezenVoertuig
                #overloop voertuigen
                for voertuig in voertuigen:
                    if voertuig.getID() == res.voertuigID:
                        #valideer of voegtuig in dezelfde zone of naburige zone ligt
                        if res.getZone() == voertuig.getZone():
                            continue
                        else:
                            zoneID = voertuig.getZone()
                            for zone in zones:
                                if zone.isBuur(zoneID):
                                    break
                                else:
                                    #Voertuig ligt niet in geldige zone
                                    res.setToegewezenVoertuig = ""
                                    #int(res_voer[3:]) is het voertuig id
                                    voertuig.deleteReservatieByID(res.getResID)
                                    #voertuigen[int(res_voer[3:])].deleteReservatieByID(res.getResID)
                                    res.toegewezen = False #klopt iets niets
                                    break
                    else:
                        continue
                pass
            else:
                continue

    def zoekChristophe(self, tijd, reservaties, voertuigen, zones):

        print(f"#reservaties {self.aantal_reservaties} #voertuigen {self.aantal_voertuigen} #zones {self.aantal_zones}")
        self.voertuig_zone = voertuigen
        self.temp_voertuig_zone = copy.deepcopy(voertuigen)
        while time.time() < tijd:
            # reservaties toewijzen
            self.reservaties_toewijzen(reservaties, zones)
            self.temp_reservaties = copy.deepcopy(reservaties)

            # wijzig random voertuig toe aan random zone
            self.temp_voertuig_zone[random.randint(0, self.aantal_voertuigen - 1)].zoneID = f"z{random.randint(0, self.aantal_zones - 1)}"

            #validatie van reservaties
            #self.valideerReservaties(reservaties, voertuigen, zones)
            self.valideerReservaties(self.temp_reservaties, self.temp_voertuig_zone, zones)


            # bereken kost
            nieuwe_kost = self.bereken_kost(self.temp_reservaties, self.temp_voertuig_zone)

            if self.save_kost > nieuwe_kost:
                self.voertuig_zone = copy.deepcopy(self.temp_voertuig_zone)
                self.save_kost = copy.deepcopy(nieuwe_kost)
                reservaties = copy.deepcopy(self.temp_reservaties)
            else:
                self.temp_voertuig_zone = copy.deepcopy(self.voertuig_zone)
                self.temp_reservaties = copy.deepcopy(reservaties)

        return self.save_kost


#####################################################################################################################
    def zoekRuben(self, tijd, reservaties, voertuigen, zones):
        kost = self.bereken_kost(reservaties, voertuigen)


        while time.time() < tijd:

            kost = self.zoekRubenRandom(reservaties, voertuigen, zones, kost)


            #kost = self.zoekRubenHillClimbing(reservaties, voertuigen, zones, kost)
        print("Ruben kost", kost)
        return kost

    def zoekRubenRandom(self, reservaties, voertuigen, zones, kost):
        save_reservaties = copy.deepcopy(reservaties)
        save_voertuigen = copy.deepcopy(voertuigen)
        save_kost = kost

        allesAutosToegewezen = False
        while not allesAutosToegewezen:
            if random.randint(0,1) == 1:
                #eerst een reservatie maken
                res = reservaties[random.randint(0, self.aantal_reservaties - 1)]
                if not res.isToegewezen():
                    autos=res.getVoertuigen()
                    len_autos = len(autos)
                    autoString = autos[random.randint(0, len_autos - 1)]
                    voertuig = self.returnVoertuigFromString(voertuigen, autoString)
                    if voertuig.kanWordenToegevoegdReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(), res.getResID()):
                        voertuig.AddReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(),res.getResID())
                        res.setToegewezenVoertuig(autoString)
                        res.setReservatieToegewezen(True)
                        voertuig.setZoneID(res.getZone())
            else:
                #buren linken
                for res in reservaties:
                    if not res.isToegewezen():
                        for autoString in res.getVoertuigen():
                            voertuig = self.returnVoertuigFromString(voertuigen, autoString)
                            if voertuig.getZone() == res.getZone():
                                if voertuig.kanWordenToegevoegdReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(), res.getResID()):
                                    voertuig.AddReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(), res.getResID())
                                    voertuig.setZoneID(res.getZone())
                                    res.setToegewezenVoertuig(autoString)
                                    res.setReservatieToegewezen(True)
                                    break

            for auto in voertuigen:
                if auto.getZone() == "":
                    allesAutosToegewezen = False
                    break
                allesAutosToegewezen = True

        niewe_kost = self.bereken_kost(reservaties, voertuigen)

        if niewe_kost < save_kost:
            save_kost=niewe_kost
            save_reservaties = copy.deepcopy(reservaties)
            save_voertuigen = copy.deepcopy(voertuigen)
        else:
            # deze weggooien
            reservaties = save_reservaties
            voertuigen = save_voertuigen

        return save_kost

    #####################################################################################################################

    def zoekRubenHillClimbing(self, reservaties, voertuigen, zones, kost):
        save_reservaties = copy.deepcopy(reservaties)
        save_voertuigen = copy.deepcopy(voertuigen)
        save_kost = kost

        res = reservaties[random.randint(0, self.aantal_reservaties - 1)]
        voertuigNamen = res.getVoertuigen()
        voertuigNaam = voertuigNamen[random.randint(0, len(res.getVoertuigen()) - 1)]
        if res.getToegewezenVoertuig() == voertuigNaam:
            return kost
            # we hebben toevallige de ToegewezenVoertuig willen heralloceren
        else:
            #voertuig los koppelen van andere reservaties
            for res2 in reservaties:
                if res2.getToegewezenVoertuig() == voertuigNaam:
                    res2.setReservatieToegewezen(False)
                    res2.setToegewezenVoertuig("")

                    for voertuig in voertuigen:
                        if voertuig.getID() == voertuigNaam:
                            voertuig.setZoneID("")
                            voertuig.deleteReservatieByID(res2.getResID())

            #voertuig toewijzen
            voertuig = self.returnVoertuigFromString(voertuigen, voertuigNaam)
            if voertuig.kanWordenToegevoegdReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(),res.getResID()):
                voertuig.AddReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(), res.getResID())
                voertuig.setZoneID(res.getZone())
                res.setToegewezenVoertuig(voertuigNaam)
                res.setReservatieToegewezen(True)

            #alle buren terug unlinken
            for res in reservaties:
                if res.isToegewezen():
                    voertuigNaam = res.getToegewezenVoertuig()
                    voertuig = self.returnVoertuigFromString(voertuigen, voertuigNaam)
                    if voertuig.getZone() != res.getZone():
                        res.setReservatieToegewezen(False)
                        res.setToegewezenVoertuig("")
                        voertuig.setZoneID("")
                        voertuig.deleteReservatieByID(res2.getResID())

            # buren proberen te koppelen
            for res in reservaties:
                if not res.isToegewezen():
                    for autoString in res.getVoertuigen():
                        voertuig = self.returnVoertuigFromString(voertuigen, autoString)
                        if voertuig.getZone() == res.getZone():
                            if voertuig.kanWordenToegevoegdReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(), res.getResID()):
                                voertuig.AddReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(), res.getResID())
                                voertuig.setZoneID(res.getZone())
                                res.setToegewezenVoertuig(autoString)
                                res.setReservatieToegewezen(True)
                                break


        niewe_kost = self.bereken_kost(reservaties, voertuigen)
        if niewe_kost < save_kost:
            save_kost = niewe_kost
            save_reservaties = copy.deepcopy(reservaties)
            save_voertuigen = copy.deepcopy(voertuigen)
        else:
            # oude herstellen weggooien
            reservaties = save_reservaties
            voertuigen = save_voertuigen

        return save_kost

    #####################################################################################################################

    def zoekJeroen(self, tijd, reservaties, voertuigen, zones):
        kost = self.bereken_kost(reservaties, voertuigen)
        zoneArray = []
        ResZone = [0 for x in range(len(zones))]
        for res in reservaties:
            for zone in zones:
                index = int(zone.getZoneID().strip('z'))
                if (res.zoneID == zone.zoneID):
                    ResZone[index]+=1
                else:
                    ResZone[index]+=0
        N=3
        if (len(zones)>20):
            N=8
        ArrLarge = sorted(range(len(ResZone)), key=lambda sub: ResZone[sub])[-N:]
        Largest = []
        for i in range(N):
            convert='z'+str(ArrLarge[i])
            Largest.append(convert)
        print("Indices list of max N elements is : " + str(ArrLarge))
        print("Indices list of N zone elements is : " + str(Largest))
        for auto in voertuigen:
            auto.setZoneID(random.choice(Largest))

        while time.time() < tijd:
            kost = self.jeroen_calc(reservaties, voertuigen, zones, kost)
            # optionele code voor voertuig aan buren
            '''for jv in voertuigen:
                jvZone = jv.getZone()
                zoneIndex = jvZone.strip('z')
                zoneIndex = int(zoneIndex)
                buren = zones[zoneIndex].getZones()
                jv.setZoneID(random.choice(buren))'''
        print("jeroen kost", kost)
        return kost

    ####################################################################################################################


    def jeroen_calc(self,reservaties, voertuigen, zones, kost):
        save_reservaties = copy.deepcopy(reservaties)
        save_voertuigen = copy.deepcopy(voertuigen)
        save_kost = kost

        allesAutosToegewezen = False
        while not allesAutosToegewezen:
            if random.randint(0, 1) == 1:
                res = reservaties[random.randint(0, self.aantal_reservaties - 1)]
                if not res.isToegewezen():
                    autos = res.getVoertuigen()
                    len_autos = len(autos)
                    autoString = autos[random.randint(0, len_autos - 1)]
                    voertuig = self.returnVoertuigFromString(voertuigen, autoString)
                    if voertuig.kanWordenToegevoegdReservatie(res.getDag(), res.getStart(),res.getStart() + res.getDuur(), res.getResID()):
                        voertuig.AddReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(),res.getResID())
                        res.setToegewezenVoertuig(autoString)
                        res.setReservatieToegewezen(True)
                        voertuig.setZoneID(res.getZone())
            else:
                # buren op check
                for res in reservaties:
                    if not res.isToegewezen():
                        for autoString in res.getVoertuigen():
                            voertuig = self.returnVoertuigFromString(voertuigen, autoString)
                            if voertuig.getZone() == res.getZone():
                                if voertuig.kanWordenToegevoegdReservatie(res.getDag(), res.getStart(),res.getStart() + res.getDuur(),res.getResID()):
                                    voertuig.AddReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(),res.getResID())
                                    res.setToegewezenVoertuig(autoString)
                                    res.setReservatieToegewezen(True)
                                    voertuig.setZoneID(res.getZone())

            for auto in voertuigen:
                if auto.getZone() == "":
                    allesAutosToegewezen = False
                    break
                allesAutosToegewezen = True

        nieuwe_kost = self.bereken_kost(reservaties, voertuigen)
        if nieuwe_kost < save_kost:
            save_kost = nieuwe_kost
            save_reservaties = copy.deepcopy(reservaties)
            save_voertuigen = copy.deepcopy(voertuigen)
        else:
            pass  # deze weggooien en op nieuw berekenen

        return save_kost


    def bereken_kost(self, reservaties, voertuigen):
        som = 0
        for res in reservaties:
            if res.isToegewezen():
                for voertuig in voertuigen:
                    if(res.getToegewezenVoertuig() == voertuig.getID()): #ToDo: optimalisatie
                        if not (res.zoneID == voertuig.zoneID):
                            som += int(res.getp2(), base=10)
                            break
            else:
                som += int(res.getp1(), base=10)

        return som

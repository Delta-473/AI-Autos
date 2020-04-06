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
            voertuig.setZoneID(f"z{random.randint(0, self.aantal_zones)}")

        self.voertuig_zone = voertuigen
        self.temp_voertuig_zone = self.voertuig_zone
        self.save_kost = self.bereken_kost(reservaties, self.voertuig_zone)

############################################################################################

    def reservaties_toewijzen(self, reservaties, zones):
        for res in reservaties:
            zoneID = int(res.zoneID[1:])
            naburigeZones = zones[zoneID].getZones()
            for voertuig in self.temp_voertuig_zone:
                if res.zoneID == voertuig.zoneID:
                    if voertuig.ID in res.voertuigen:
                        if voertuig.kanWordenToegevoegdReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(), res.getResID()):
                            voertuig.AddReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(),res.getResID())
                            res.voertuigID = voertuig.ID
                            res.toegewezen = True
                            break
                else:
                    for buren in naburigeZones:
                        if buren == voertuig.ID:
                            if voertuig.kanWordenToegevoegdReservatie(res.getDag(), res.getStart(),res.getStart() + res.getDuur(), res.getResID()):
                                voertuig.AddReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(),res.getResID())
                                res.voertuigID = voertuig.ID
                                res.toegewezen = True
                                break

    def zoekChristophe(self, tijd, reservaties, voertuigen, zones):

        print(f"#reservaties {self.aantal_reservaties} #voertuigen {self.aantal_voertuigen} #zones {self.aantal_zones}")
        self.voertuig_zone = voertuigen
        self.temp_voertuig_zone = voertuigen
        while time.time() < tijd:
            # reservaties toewijzen
            self.reservaties_toewijzen(reservaties, zones)

            # wijzig random voertuig toe aan random zone
            # self.temp_voertuig_zone[random.randint(0, self.aantal_voertuigen - 1)].zoneID = f"z{random.randint(0, self.aantal_zones - 1)}"

            # bereken kost
            nieuwe_kost = self.bereken_kost(reservaties, self.temp_voertuig_zone)

            if self.save_kost > nieuwe_kost:
                self.voertuig_zone = self.temp_voertuig_zone
                self.save_kost = nieuwe_kost
            else:
                self.temp_voertuig_zone = self.voertuig_zone

        return self.save_kost


#####################################################################################################################
    def zoekRuben (self, tijd, reservaties, voertuigen, zones):
        kost = self.bereken_kost(reservaties, voertuigen)
        while time.time() < tijd:
            kost = self.zoekRubenRandom(reservaties, voertuigen, zones, kost)

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
                #buren op checkit
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

    def zoekRubenHillClimbing(self, tijd, reservaties, voertuigen, zones, kost):
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


        niewe_kost = self.bereken_kost(reservaties, voertuigen)
        if niewe_kost < save_kost:
            save_kost = niewe_kost
            save_reservaties = copy.deepcopy(reservaties)
            save_voertuigen = copy.deepcopy(voertuigen)
        else:
            # deze weggooien
            reservaties = save_reservaties
            voertuigen = save_voertuigen

        return save_kost

    #####################################################################################################################

    def find3largest(self, arr, output_array):
        arr_size = len(arr)
        third = first = second = 0
        fi = si = ti = ''

        for i in range(0, arr_size):
            # If current element is greater than first
            if (arr[i] > first):
                third = second
                second = first
                first = arr[i]
                si=fi
                fi='z'+str(i)

                # If arr[i] is in between first and second then update second
            elif (arr[i] > second):
                third = second
                second = arr[i]
                si='z'+str(i)

            elif (arr[i] > third):
                third = arr[i]
                ti='z'+str(i)

        print("Three largest elements are", first, second, third)
        print("Three largest elements are located at index", fi, si, ti)
        output_array.append(fi)
        output_array.append(si)
        output_array.append(ti)

    def zoekJeroenVersie(self, tijd, reservaties, voertuigen, zones):
        resID = 0;
        zoneArray = []
        ResZone = [0 for x in range(len(zones))]
        for res in reservaties:
            for zone in zones:
                index = int(zone.getZoneID().strip('z'))
                if (res.zoneID == zone.zoneID):
                    ResZone[index]+=1
                else:
                    ResZone[index]+=0

        self.find3largest(ResZone,zoneArray)
        #zoneArray = ["z0", "z4", "z2"]
        for auto in voertuigen:
            RandZone = zoneArray[math.floor(random.random() * len(zoneArray))]
            auto.setZoneID(RandZone)
        while time.time() < tijd:
            save_reservaties = copy.deepcopy(reservaties)
            save_voertuigen = copy.deepcopy(voertuigen)
            save_kost = self.bereken_kost(reservaties, voertuigen)
            # for auto in voertuigen:
            #  zoneArray = ["z0", "z2", "z4"]
            # RandZone = zoneArray[math.floor(random.random() * len(zoneArray))]
            # auto.setZoneID(RandZone)
            allesAutosToegewezen = False
            while not allesAutosToegewezen:
                res = reservaties[resID]
                resID+1;
                if not res.isToegewezen():
                    autos = res.getVoertuigen()
                    len_autos = len(autos)
                    autoString = autos[random.randint(0, len_autos)]
                    voertuig = self.returnVoertuigFromString(voertuigen, autoString)
                    if voertuig.kanWordenToegevoegdReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(), res.getResID()):
                        voertuig.AddReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(), res.getResID())
                        res.setToegewezenVoertuig(autoString)
                        res.setReservatieToegewezen(True)
                        RandZone = zoneArray[math.floor(random.random() * len(zoneArray))]
                        voertuig.setZoneID("z0")

                else:
                    # buren op check
                    for res in reservaties:
                        if not res.isToegewezen():
                            for autoString in res.getVoertuigen():
                                voertuig = self.returnVoertuigFromString(voertuigen, autoString)
                                if voertuig.getZone() == res.getZone():
                                    if voertuig.kanWordenToegevoegdReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(), res.getResID()):
                                        voertuig.AddReservatie(res.getDag(), res.getStart(), res.getStart() + res.getDuur(), res.getResID())
                                        res.setToegewezenVoertuig(autoString)
                                        res.setReservatieToegewezen(True)

                for auto in voertuigen:
                    if auto.getZone() == "":
                        allesAutosToegewezen = False
                        break
                    allesAutosToegewezen = True

            niewe_kost = self.bereken_kost(reservaties, voertuigen)
            if niewe_kost < save_kost:
                save_kost = niewe_kost
                save_reservaties = copy.deepcopy(reservaties)
                save_voertuigen = copy.deepcopy(voertuigen)
            else:
                pass  # deze weggooien en op nieuw berekenen

        return save_kost







    ####################################################################################################################

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

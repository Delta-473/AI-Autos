from models import data
import numpy as np

from models.VoertuigBezet import VoertuigBezet

class Voertuig():
    ID= ""
    zoneID= ""
    voertuig_bezettingen = []

    def setZoneID(self,zone):
        self.zoneID=zone

    def __init__(self,ID):
        self.ID=ID
        #print("voertuig made",self.id)

    def getID(self):
        return self.ID

    def __str__(self):
        return f"Voertuig ID: {self.ID} en zone ID: {self.zoneID}"

    def getZone(self):
        return self.zoneID

    def getReservaties(self):
        return self.voertuig_bezettingen

    def getAantalReservaties(self):
        return len(self.voertuig_bezettingen)

    def deleteReservatieByID(self, ID):
        aantalRes = len(self.voertuig_bezettingen)
        for i in range(0, aantalRes - 1):
            if(self.voertuig_bezettingen[i].resID == ID):
                self.voertuig_bezetting = np.delete(self.voertuig_bezettingen, i, 0)
                break

    def AddReservatie(self, dag, start, einde, resID):
        self.voertuig_bezettingen.append(VoertuigBezet(dag, start, einde, resID))

    def kanWordenToegevoegdReservatie(self,dag2, start2, einde2, resID):
        lukt=True
        for bezetting in self.voertuig_bezettingen:
            if bezetting.getResID() == resID:
                return True #deze reservatie zit er al in
            if bezetting.getDag() != dag2:
                continue    #als we 2 verschillende dagen aan het vergelijken zijn dan volgende
            if (start2 < bezetting.getStart()) and (einde2 < bezetting.getStart()):  # nieuwe bezetting(2) kan voor de oude(huidige)
                continue
            if bezetting.getEinde() < start2:  # nieuwe bezetting (2) kan na de oude bezetting( huidige)
                continue
            else:
                lukt=False
        return lukt



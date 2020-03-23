#def NIETTOEGEWEZEN False
#def TOEGEWEZEN True
class Reservatie():
    resId=""
    zoneId=""
    dag=0
    start=0
    duur=0
    voertuigen=""
    voertuigenToegewezenVlag
    pentalty1=0
    pentalty2=0
    voertuigId = ""
    toegewezen=False


    def __init__(self, resId, zoneId, dag,  start, duur, voertuigen, p1,p2):
        self.resId=resId
        self.zoneId=zoneId
        self.dag=dag
        self.start=start
        self.duur=duur
        self.voertuigen=voertuigen
        for x in range (len(self.voertuigen)):
            voertuigenToegewezenVlag.append(False)#NIETTOEGEWEZEN)

        self.pentalty1=p1
        self.pentalty2=p2

    def getVoertuigIndex(self,index):
        return voertuigen[index]

    def setVoertuigToegewezen(self,index):
        voertuigenToegewezenVlag[index]=True

    def setVoertuigNietToegewezen(self,index):
        voertuigenToegewezenVlag[index]=False

    def checkVoertuigToegewezen(self,index):
        return voertuigenToegewezenVlag[index]

    def getVoertuigFlag(self):
        return self.voertuigenToegewezenVlag


    def getVoertuigen(self):
        return self.voertuigen

    def selfCheck(self):
        for vlag in self.voertuigenToegewezenVlag:
            if (vlag==False):
                self.toegewezen=False
                return False
        self.toegewezen=True
        return True

    def getresId(self):
        return self.resId

    def getZone(self):
        return self.zoneId

    def getDag(self):
        return self.dag

    def getStart(self):
        return self.start

    def getDuur(self):
        return self.duur

    def getP1(self):
        return self.pentalty1

    def getP2(self):
        return self.pentalty2

    def __str__(self):
        return f"resID: {self.resId}, zoneID: {self.zoneId}, dag: {self.dag}, start: {self.start}, duur: {self.duur}" \
               f", voertuigen: {self.voertuigen}, penalty1: {self.pentalty1}, penalty2: {self.pentalty2}"

    def isToegewezen(self):
        return self.toegewezen

    def getp1(self):
        return self.pentalty1

    def getp2(self):
        return self.pentalty2

    def getToegewezenVoertuig(self):
        return self.voertuigId

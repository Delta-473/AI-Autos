class VoertuigBezet():

    dag = ""
    start = ""
    einde = ""
    resID = ""

    def __init__(self):
        pass
    
    def __str__(self):
        return f"Dag: {self.dag}, Start: {self.start}, Einde: {self.einde}, Reservatie ID: {self.resID}"

    def getDag(self):
        return self.dag

    def setDag(self, dag):
        self.dag = dag

    def getStart(self):
        return self.start

    def setStart(self, start):
        self.start = start

    def getEinde(self):
        return self.einde

    def setEinde(self, einde):
        self.einde = einde

    def getResID(self):
        return self.resID

    def setResID(self, resID):
        self.resID = resID

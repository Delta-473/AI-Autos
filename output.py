from models.Reservatie import Reservatie
from models.Zone import Zone
from models.Voertuig import Voertuig

class Output():
    file = None
    #log= open('data/log_jeroen.txt', "a+")
    buffer = ""

    def __init__(self, filepath):
        self.file = open(filepath, "w")

    def schrijven(self, penaltyscore, reservaties, voertuigen):

        #penaltyscore
        self.buffer = f"{penaltyscore} \n"
        #self.log.write(f"{penaltyscore} \n")

        #Vehicle assignments
        self.buffer += "+Vehicle assignments\n"
        for voertuig in voertuigen:
            self.buffer += f"{voertuig.ID};{voertuig.zoneID}\n"

        #Assigned requests
        self.buffer += "+Assigned requests\n"
        for reservatie in reservaties:
            if reservatie.isToegewezen():
                self.buffer += f"{reservatie.resID};{reservatie.getToegewezenVoertuig()}\n"

        #Unassigned requests
        self.buffer += "+Unassigned requests\n"
        for reservatie in reservaties:
            if not reservatie.isToegewezen():
                self.buffer += f"{reservatie.resID}\n"

        self.file.write(self.buffer)
        self.file.close()
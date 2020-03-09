from models.Reservatie import Reservatie
from models.Zone import Zone
from models.Voertuig import Voertuig

class Output():
    file = None
    buffer = ""

    def __init__(self, filepath):
        self.file = open(filepath, "w")

    def schrijven(self, penaltyscore, reservaties, voertuigen):

        #penaltyscore
        self.buffer = f"{penaltyscore} \n"

        #Vehicle assignments
        self.buffer += "+Vehicle assignments\n"
        for voertuig in voertuigen:
            self.buffer += f"{voertuig.id};{voertuig.zoneId}\n"

        #Assigned requests
        self.buffer += "+Assigned requests\n"
        for reservatie in reservaties:
            if reservatie.voertuigId != "":
                self.buffer += f"{reservatie.resId};{reservatie.voertuigId}\n"

        #Unassigned requests
        self.buffer += "+Unassigned requests\n"
        for reservatie in reservaties:
            if reservatie.voertuigId == "":
                self.buffer += f"{reservatie.resId}\n"

        self.file.write(self.buffer)
        self.file.close()


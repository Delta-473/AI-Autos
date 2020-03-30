from models.Reservatie import Reservatie
from models.Zone import Zone
from models.Voertuig import Voertuig

class Inlees():


    def __init__(self, location):
        self.location=location
        self.file=open((self.location),"r+")
        self.cars = []
        self.res = []
        self.zones = []

    def lees(self, reservaties, zones, voertuigen):
        line=self.file.readline()

        #Reversaties inlezen
        print("contens of line",line)
        line=line.split(': ')
        aantalRequests = int(line[1])
        #print(aantalRequests)
        for i in range(aantalRequests):
            line=self.file.readline()
            line=line.split(";")

            request=line[0]
            zone=line[1]
            dag=int(line[2])
            start=int(line[3])
            duur=int(line[4])
            carsLine=line[5].split(",")
            cars=[]
            for c in carsLine:      # array van cars
                cars.append(c)
            penalty1=line[6]
            penalty2=line[7]

            res=Reservatie(request,zone,dag,start,duur,cars,penalty1,penalty2)
            print(res)
            reservaties.append(res)
            self.res.append(res)

        # Zones inlezen
        line=self.file.readline()
        line=line.split(': ')
        aantalZones = int(line[1])

        for j in range(aantalZones):
            line=self.file.readline()
            line=line.split(';')
            eigenZone=line[0]
            zoneBuurLine=line[1].split(',')
            zoneBuur=[]
            for buur in zoneBuurLine:
                zoneBuur.append(buur)
            zone=Zone(eigenZone,zoneBuur)
            zones.append(zone)
            self.zones.append(zones)


        #Voertuigen inlezen
        line=self.file.readline()
        line=line.split(': ')
        aantalCars = int(line[1])

        for k in range(aantalCars):
            line=self.file.readline()
            voertuig=line.rstrip('\n')
            car=Voertuig(voertuig)
            voertuigen.append(car)
            self.cars.append(voertuig)

        line=self.file.readline()
        line=line.split(': ')
        aantalDagen = int(line[1])
        # print(aantalDagen)

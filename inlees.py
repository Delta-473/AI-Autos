from models.Reservatie import Reservatie
from models.Zone import Zone
from models.Voertuig import Voertuig

class Inlees():
    file=None
    location=""
    
    def __init__(self, location):
        self.location=location
        self.file=open((self.location),"r+")
        
       
    
    def lees(self):
        line=self.file.readline()
        
        print("contens of line",line)
        line=line.split(': ')
        aantalRequests = int(line[1])
        print(aantalRequests)
        requests=[]
        for i in range(aantalRequests):
            line=self.file.readline()
            line=line.split(";")
            request=line[0]
            zone=line[1]
            dag=int(line[2])
            start=int(line[3])
            duur=int(line[4])
            cars=line[5]
            penalty1=line[6]
            penalty2=line[7]
            res=Reservatie(request,zone,dag,start,duur,cars,penalty1,penalty2)
            res.__str__()
            requests.append(res)
            
        line=self.file.readline()
        line=line.split(': ')
        aantalZones = int(line[1])
        zones=[]
        for j in range(aantalZones):
            line=self.file.readline()
            print(line)
            line=line.split(';')
            print(line[0])
            print(line[1])
            eigenZone=line[0]
            aanliggendeZone=line[1]
            zone=Zone(eigenZone,aanliggendeZone)
            zone.__str__()
            zones.append(zone)
        
        line=self.file.readline()
        line=line.split(': ')
        aantalCars = int(line[1])
        cars=[]
        for k in range(aantalCars):
            line=self.file.readline()
            print(line)
            voertuig=line
            car=Voertuig(voertuig)
            cars.append(car)
            
        line=self.file.readline()
        line=line.split(': ')
        aantalDagen = int(line[1])
        print(aantalDagen)
        



def main():
    print("program started")
    inlees=Inlees("data/100_5_14_25.csv")
    inlees.lees()
    
main()
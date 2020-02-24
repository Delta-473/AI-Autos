from Reservatie import Reservatie
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
        print('contens of line[0]',line[0])
        print('contens of line[1]',line[1])
        aantalRequests = int(line[1])
        print(aantalRequests)
        for i in range(aantalRequests):
            line=self.file.readline()
            line=line.split(";")
            requests=line[0]
            zone=line[1]
            dag=int(line[3])
            start=int(line[4])
            duur=int(line[5])
            cars=line[6]
            penalty1=line[7]
            penalty2=line[8]
            res=Reservatie(requests,zone,dag,start,duur,cars,penalty1,penalty2)
            res.__str__()
            



def main():
    print("program started")
    inlees=Inlees("100_5_14_25.csv")
    inlees.lees()
    
main()
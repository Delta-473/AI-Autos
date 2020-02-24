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
        




def main():
    print("program started")
    inlees=Inlees("100_5_14_25.csv")
    inlees.lees()
    
main()
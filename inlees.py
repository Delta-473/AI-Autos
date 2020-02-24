from readFile import ReadFile


class inlees(location):
    file=None
    
    def __init__(location):
        self.location=location
        self.file=open((self.location+"txt"),"r+")    
                   
       
    
    def lees():
        line=self.file.readline()
        
        print("contens of line",line)
        nr=nr.split(': ')
        print('contens of line[0]',nr[0])
        print('contens of line[1]',nr[1])
        

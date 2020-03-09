import argparse

from inlees import Inlees
from output import Output


class Main():

    ifilepath = ""
    ofilepath = ""
    penaltyscore = 0

    reservaties=[]
    zones=[]
    voertuigen=[]

    def __init__(self):
        pass

    def parsearguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", help="Geef pad naar de input file")
        parser.add_argument("-o", help="Geef pad naar de output file")
        args = parser.parse_args()
        self.ifilepath = args.i
        self.ofilepath = args.o
        print("python3 main.py -i data/toy1.csv -o data/outputcsv")

    def main(self):
        self.parsearguments()


        inlees = Inlees(self.ifilepath)
        inlees.lees(self.reservaties, self.zones, self.voertuigen)


        output = Output(self.ofilepath)

        output.schrijven(self.penaltyscore, self.reservaties, self.voertuigen)


Main().main()

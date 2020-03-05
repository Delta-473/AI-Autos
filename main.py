import argparse

from inlees import Inlees
from output import Output


class Main():

    ifilepath = ""
    ofilepath = ""
    penaltyscore = 0

    def __init__(self):
        pass

    def parsearguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", help="Geef pad naar de input file")
        parser.add_argument("-o", help="Geef pad naar de output file")
        args = parser.parse_args()
        self.ifilepath = args.i
        self.ofilepath = args.o

    def main(self):
        self.parsearguments()
        inlees = Inlees(self.ifilepath)
        output = Output(self.ofilepath)
        reservaties = []
        zones = []
        voertuigen = []

        inlees.lees(reservaties, zones, voertuigen)

        output.schrijven(self.penaltyscore, reservaties, voertuigen)


Main().main()

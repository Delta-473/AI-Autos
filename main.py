import argparse
import time
import random
import copy


from inlees import Inlees
from output import Output
from zoekalgoritme import zoekalgoritme


class Main():

    ifilepath = ""
    ofilepath = ""
    penaltyscore = 0
    time = 0
    seed = 0
    threads = 1

    reservaties=[]
    zones=[]
    voertuigen=[]

    def __init__(self):
        pass
    # parse argument voor gebruik in program. inputfile, output, time, rand_seed, threads
    def parsearguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("input_file", help="Geef pad naar de input file")
        parser.add_argument("solution_file", help="Geef pad naar de output file")
        parser.add_argument("time_limit", help="tijd waarna het algoritme moet stoppen, uitgedrukt in seconde")
        parser.add_argument("random_seed", help="random seed waarde")
        parser.add_argument("num_threads", help="het maximum aantal threads dat het algoritme mag gebruiken")
        args = parser.parse_args()
        self.ifilepath = args.input_file
        self.ofilepath = args.solution_file
        self.time = args.time_limit
        self.seed = args.random_seed
        self.threads = args.num_threads #ToDo: not implemented


    def main(self):
        self.parsearguments()

        random.seed(self.seed)
        stoptijd = time.time() + float(self.time)
        halvestop = time.time() + float(self.time)/2

        inlees = Inlees(self.ifilepath)
        inlees.lees(self.reservaties, self.zones, self.voertuigen)

        zoek = zoekalgoritme(self.reservaties, self.voertuigen, self.zones)
        #self.penaltyscore = zoek.zoekChristophe(stoptijd, self.reservaties, self.voertuigen, self.zones)


        penaltyscoreRuben = zoek.zoekRuben(halvestop, self.reservaties, self.voertuigen, self.zones)
        RubenRes= self.reservaties
        RubenCar = self.voertuigen
        RubenZone =  self.zones

        penaltyscoreJeroen = zoek.zoekJeroen(stoptijd, self.reservaties, self.voertuigen, self.zones)

        if (penaltyscoreRuben < penaltyscoreJeroen):
            self.penaltyscore= penaltyscoreRuben
            self.reservaties = RubenRes
            self.voertuigen = RubenCar
            self.zones = RubenZone

        else:
            self.penaltyscore= penaltyscoreJeroen
        #self.penaltyscore = zoek.bereken_kost(self.reservaties, self.voertuigen)

        output = Output(self.ofilepath)

        output.schrijven(self.penaltyscore, self.reservaties, self.voertuigen)
    # java -jar validator.jar ./data/toy1.csv ./data/test.csv

Main().main()

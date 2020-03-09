

def kost(self,reservaties):
    som=0
    for res in reservaties:
        if(res.isToegewezen() ):
            if(not(res.getzone() == res.toegewezenVoertuig().getzone())):
                sum+=res.getp2()
        else:
            sum+=res.getp1()

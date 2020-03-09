

    def kost(self,reservaties):
        som=0
        for res in reservaties:
            if(res.isToegewezen() and res.getzone() == res.toegewezenVoertuig().getzone()):
                sum+=res.getp2()
            else if(not (res.isToegewezen())):
                sum+=res.getp1()

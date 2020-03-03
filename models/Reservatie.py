class Reservatie():
    resId=""
    zoneId=""
    dag=0
    start=0
    duur=0
    voertuigen=""
    pentalty1=0
    pentalty2=0

    def __init__(self, resId, zoneId, dag,  start, duur, voertuigen, p1,p2):
        self.resId=resId
        self.zoneId=zoneId
        self.dag=dag
        self.start=start
        self.duur=duur
        self.voertuigen=voertuigen
        self.pentalty1=p1
        self.pentalty2=p2

    def __str__(self):
        return "resID: %s, zoneID: %s, dag: %s, start: %s, duur: %s, voertuigen: %s, penalty1: %s, penalty2: %s" % \
               (self.resId, self.zoneId, self.dag, self.start, self.duur, self.voertuigen, self.pentalty1, self.pentalty2)


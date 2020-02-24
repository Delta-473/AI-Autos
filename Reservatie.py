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
        self.zoneid=zoneId
        self.dag=dag
        self.start=start
        self.duur=duur
        self.voertuigen=voertuigen
        self.pentalty1=p1
        self.pentalty2=p2
       
    def  __str__(self):
        print("resId",self.resId)
        print("zoneid",self.zoneId)
        print("dag",self.dag)
        print("start",self.start)
        print("duur",self.duur)
        print("voertuigen",self.voertuigen)
        print("pentalty1",self.pentalty1)
        print("pentalty2",self.pentalty2)

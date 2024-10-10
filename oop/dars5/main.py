class Car:
    def __init__(self, nomi,markasi, yili, dvigateli,rangi,narxi,ot_kuchi, rasxod):
        self.nomi=nomi
        self.dvigateli=dvigateli
        self.yili=yili
        self.markasi = markasi
        self.rangi=rangi
        self.ot_kuchi=ot_kuchi
        self.rasxod = rasxod
        self.narxi = narxi

    def car_narx(self):
        print(f"{self.markasi} yili {self.yili} ekan narxi {self.narxi}")

    def car_kami(self):
        self.narxi_kami = self.narxi - (2024 - self.yili)*self.narxi*0.02
        print(f"mashina kamaygan narxi {self.narxi_kami}")

gentra = Car("GM","Gentra",2024,"IYD","oq",17000,105,12)
nexia = Car("GM","Nexia 3",2018,"IYD","qora",12000,105,12)
malibu = Car("GM","Malibu turbo ",2017,"IYD","qora",25000,250,14)
             
gentra.car_narx()
gentra.car_kami()
nexia.car_narx()
nexia.car_kami()
malibu.car_narx()
malibu.car_kami()



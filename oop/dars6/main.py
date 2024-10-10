class Shaxs :   
    def __init__(self,isim,familyasi,pasporti,tugilgankuni,yili):
        self.isim = isim.title()
        self.familyasi = familyasi
        self.pasporti = pasporti
        self.tugilgankuni = tugilgankuni
        self.yili = yili
    def shaxs_info (self):
        info=f"isim {self.isim}, familyasi {self.familyasi},pasporti {self.pasporti}, tugilgankuni {self.tugilgankuni}, yili {self.yili} "
        return info
    def shaxsyoshi(self):
        self.yosh=2024-int(self.yili)
        return self.yosh

shaxs1=Shaxs(
    isim="Davronbek",
    familyasi="Kayumov",
    pasporti="AB8310721",
    tugilgankuni="06",
    yili="2001",
    
    )

shaxs2=Shaxs(
    isim="Alisher",
    familyasi="Salohiddinov",
    pasporti="AC8391269",
    tugilgankuni="18",
    yili="2004",
    )

shaxs3=Shaxs(
    isim="Sardor",
    familyasi="Murodov",
    pasporti="AC8761269",
    tugilgankuni="25",
    yili="2003",
    )

# print (shaxs1.shaxs_info())
# print (shaxs2.shaxs_info())
# print (shaxs3.shaxs_info())

class Talaba(Shaxs):
   def info().__init__(i_, f_, t_, guruh):
        super().__init__(i_, f_, t_)
        self.guruh = guruh

    def t_info(self):
       
    


class Hudud:
    def __init__(self, nom, maydon, boshliq, markaz):
        self.nom=nom
        self.maydon=maydon
        self.boshliq=boshliq
        self.markaz=markaz

    def hudud_info(self):
        info = f"""
                Hudud nomi:    {self.nom}
                Hudud maydoni: {self.maydon}
                Hudud markazi: {self.markaz}
                Hudud ma'suli: {self.boshliq}
                """
        return info

# hudud1 = Hudud(nom="Baliqchi",maydon="100 gektar",boshiq="Sazan",markaz="Baliqchi petak")
# print(hudud1.hudud_info())
    
class Shahar(Hudud):
    def __init__(self, nom, maydon, boshliq, markaz):
        super().__init__( nom, maydon, boshliq, markaz)
        self.hokim = boshliq


    def shahar_info(self):
        info = f"""
                Shahar nomi:    {self.nom}
                Shahar maydoni: {self.maydon}
                Shahar markazi: {self.markaz}
                Shahar hokimi: {self.hokim}
                """
        return info

hudud1 = Shahar(nom="Baliqchi",maydon="100 gektar",boshliq="Sazan",markaz="Baliqchi petak")
print(hudud1.shahar_info())

class Viloyat (Shahar):
    def __init__(self, nom, maydon, boshliq, markaz,partnumber):
        super().__init__( nom, maydon, boshliq, markaz)
        self.partyanumber = partnumber


    def viloyat_info(self):
        info = f"""
                Viloyat nomi:    {self.nom}
                Viloyat maydoni: {self.maydon}
                Viloyat markazi: {self.markaz}
                Viloyat hokimi: {self.hokim}
                Viloyat raqami: {self.partyanumber}
                """
        return info

hudud1 = Viloyat(nom="Baliqchi",maydon="100 gektar",boshliq="Sazan",markaz="Baliqchi petak",partnumber="50")
print(hudud1.viloyat_info())
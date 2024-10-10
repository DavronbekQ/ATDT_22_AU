# class Transformer:
#     def __init__(self,x):
#         self.x = x
#     def run(self):
#         self.x = self.x+1
# optimes=Transformer
# optimes.run()
# print(optimes.x)

class Gun:
    def __init__(self):
        self.reload()
    def fire(self):
        self.count=self.count-1
        print("bitish,bitish",self.count)
    def reload(self):
        self.count=50

class Transformer:
    def __init__(self,gunleft,gunright):
        self.gunleft=gunright
        self.gunright=gunleft
    def fire(self):
        self.gunright.fire()
        self.gunleft.fire()
    def sword(self):
        print("shitik,shitik salomat")

gun1=Gun()
gun2=Gun()
optimes=Transformer(gun1,gun2)
# optimes.fire()
# optimes.sword()

class Avtobot(Transformer):
    def transform (self):
        print("Mashinaga aylandi")
optimes=Avtobot(gun1,gun2)
optimes.fire()
optimes.transform()
optimes.sword()
class Disepticon(Transformer):
    def transform(self):
        print("samalyotga aylandi")
megatron=Disepticon(gun1,gun2)
megatron.fire()
megatron.fire()



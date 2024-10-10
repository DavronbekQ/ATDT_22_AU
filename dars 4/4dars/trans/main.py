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
gun1=Gun()
gun2=Gun()
optimes=Transformer(gun1,gun2)
optimes.fire()
print(optimes.count)
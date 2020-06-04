from abc import abstractmethod,ABC
class bmw(ABC):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print("stating a car")
    def stop(self):
        print("stoping a car")

    @abstractmethod                             #cant make objects for this         jimp to use drive in child 
    def drive(self):
        pass

class three(bmw):                               #inheriting bmw
    def __init__(self,control,make,model,year):
        super().__init__(make,model,year)
        self.control=control
    def display(self):
        print(self.control)
    def start(self):
        super().start()             #paren's start          #overriding
        print("start")
    def drive(self):
        print("three")

t=three(True,"bmw","i",2020)
print(t.control)
print(t.model)
print(t.start())
print(t.stop())
print(t.display())
print(t.drive())

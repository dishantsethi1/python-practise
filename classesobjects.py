                            #classes and objects


class product:
    def __init__ (self):
        self.name="iphone"
        self.description="osm"
        self.price=100000
    def display(self):
        print(self.name)


p1=product()                                     #object
#p1.display()


'''class course:
    def __init__(self,name,ratings):             #parameter
        self.ratings=ratings
        self.name=name
    def average(self):
        ratingss=len(self.ratings)
        average=sum(self.ratings)/ratingss
        print(average)

c=course("python",[5,5,5])
print(c.name)
print(c.ratings)
c.average()'''



class programmer:
    def setname(self,m):
        self.name=m
    def getname(self):
        return self.name
    def setsalary(self,sal):
        self.salary =sal
    def getsalary(self):
        return self.salary
    def settech(self,techs):
        self.techh=techs
    def gettech(self):
        return self.techh

p=programmer()
p.setname("dishant")
p.setsalary(100000)
p.settech(["py","c++"])

#print(p.getname())
#print(p.gettech())
#print(p.getsalary())

class student:
    major="cse"
    def __init__(self,rn,n):
        self.name=n
        self.roolno=rn

s=student(2,"dish")
#print(s.major)
#print(s.name)
#print(s.roolno)

                                #count no of objects


class obj:
    c=0
    def __init__(self):
        obj.c+=1
    @staticmethod
    def display():
        print(obj.c)
o1=obj()
o2=obj()
#obj.display()



                                #innerclass

class car:
    def __init__(self,make,year):
        self.make=make
        self.year=year

    class engine:
        def __init__(self,un):
            self.no=un
        def start(self):
            print("engine started")


c=car("b",2000)
e=c.engine(123)
e.start()

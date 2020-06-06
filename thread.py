from  threading import *
from time import sleep

#print(threading.current_thread().getName())         #to know current_thread

'''def display():
    i=0
    print(current_thread().getName())
    while i<=1:
        print(i)
        i+=1
print(current_thread().getName())
t=Thread(target=display)
t.start()





#new method
class mythread(Thread):
    def run(self):
        i=0
        while i<=1:
            print(i)
            i+=1

t1=mythread()
t1.start()




#new method
class mythread1:
    def display1(self):
        i=0
        print(current_thread().getName())
        sleep(1)
        while i<=1:
            print(i)
            i+=1

obj=mythread1()
t2=Thread(target=obj.display1)
t2.start()'''








'''class bookmybus:
    def __init__(self,ase):
        self.ase=ase
        self.l=Lock()                               #locking for particular thread

    def buy(self,sr):
        self.l.acquire()
        print("available seats",self.ase)             #sr=seats  requested
        if(self.ase>=sr):
            print("confirming a seat")
            print("processing ")
            print("printing a ticket")
            self.ase=self.ase-sr
        else:
            print("no seats available")
        self.l.release()


b1=bookmybus(10)
r1=Thread(target=b1.buy,args=(3,))
r2=Thread(target=b1.buy,args=(4,))
r3=Thread(target=b1.buy,args=(5,))
r1.start()
r2.start()
r3.start()'''





class producer:
    def __init__(self):
        self.pl=[]                          #prodducts list
        #self.op=False                        #orders placed
        self.c=Condition()
    def produce(self):
        self.c.acquire()  #
        for i in range(1,5):
            self.pl.append("product"+str(i))
            sleep(1)
            print("item added ")
        self.c.notify()             #or u can use self.op==True
        self.c.release()

class consumer:
    def __init__(self,prod):
        self.prod=prod
    def consume(self):
        self.prod.c.acquire()                   # or ca n use while seld.prod.op==False: sleep(0)
        self.prod.c.wait(timeout=0)
        self.prod.c.release()
        print("orders shipped ",self.prod.pl)


p=producer()
c=consumer(p)

t1=Thread(target=p.produce)
t2=Thread(target=c.consume)

t1.start()
t2.start()

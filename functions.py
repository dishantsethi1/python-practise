from functools import reduce

#def average(a,b):
    #return (a+b)/2

#x=average(10,20)
#print(x)

def calc(a,b):                      #defining a function
    x=a+b
    y=a-b
    z=a*b
    q=a/b
    return x,y,z,q                  #as tuple

result=calc(10,5)
#print(result)





        #global and local usage
r=1
def display():
    r=2
    print(r)
    print(globals()['r'])           #to access global r

#print(r)
t=display
#t()                                 #another way to invoke





        #function inside another

def display1(name):
    def message():
        return "hello "
    result=message()+name
    return result

#print(display1("dishant"))



        #function as parameter

def display2(fun):
    return "hello "+fun
def name1():
    return "dishant"

#print(display2(name1()))

                            #lambda




'''l=lambda x:'yes ' if x%2==0 else 'no'                #short functions

print(l(10))

c=lambda a,b:a+b
print(c(10,20))'''

lst2=[10,2,44,35,67]
res=list(filter(lambda x:x%2==0,lst2))                      #filter
#print(res)



lst3=[2,3,4,5]
res1=list(map(lambda n:n*2,lst3))                               # map
#print(res1)


lst4=[5,10,15,20]                   #reduce   using         from functools import reduce
res2=reduce(lambda x,y:x+y,lst4)
#print(res2)





                                #decorator

def decor(fun):
    def inner():
        result=fun()
        return result*2
    return inner


def num():
    return 5

resu=decor(num)                         #can also use @decor
#print(resu())


                            #generators
def customg(x,y):
    while x<y:
        yield x
        x+=1
                                            #custom ranges  same as range
res4=customg(4,8)

for i in res4:print(i)

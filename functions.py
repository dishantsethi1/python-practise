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

print(display2(name1()))

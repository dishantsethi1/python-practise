import logging

logging.basicConfig(filename="mylog.log",level=logging.DEBUG)
                      #will show all

try:
    f=open("myfile","w")
    a,b=[int(x) for x in input("enter two num").split() ]
    logging.info("info")
    c=a/b
    print(c)
    f.write("%d" %c)
except ZeroDivisionError:
    print("cant divide by zero")
    logging.error("error")
else:                                               #only when no exception
    print("success")
finally:                                            #will always work
    f.close
    print("completed")
print("done")

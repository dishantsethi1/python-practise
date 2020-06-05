import time
st=time.perf_counter()                  #performance time calculator
print(st)
epoch=time.time()
print(epoch)                        # give inseconds


#time.sleep(3)           #will work after 3 seconds
t=time.ctime(epoch)                 #exact date and time
print(t)

#date not working
#i dont know why it is not working
et=time.perf_counter()
print(et-st)                        #total execution time it took

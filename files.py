import os,sys


''''f=open("myfile.txt","w")                 #writing files
print("write # to exit")
s=''
while  s !='#':                         #will work till you enter #
    s=input()
    f.write(s)
f.close()'''

if os.path.isfile('myfile.txt'):
    f=open("myfile.txt","r")                    #reading files
    s=f.read()
    print(s)
    f.close()
else:
    print("no file ")
    sys.exit()

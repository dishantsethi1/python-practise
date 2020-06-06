'''NOthing is working from here i dont know why'''






'''from urllib.request import *


try:
    url=urllib.request.urlopen("https://www.python.org/")
    content=url.read()
except urllib.error.HTTPError:
    print("not found")
    exit()


f=open("python.html","wb")
f.write(content)
f.close()


            #downloading image
url="https://www.python.org/static/img/python-logo.png"

urllib.request.urlretrieve(url,"python.png")'''









'''import socket
host='localhost'
port=4000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)                 #1 is no of connecions
c,addr=s.accept()
print("coneection:",str(addr))
c.send(b"hello how are you")                #converted into binary
c.close()'''










            #sending emails

import smtplib

from email.mime.text import MIMEText
body="dishant sethi"

msg=MIMEText(body)
msg['From']="dishantsethi@gmail.com"
msg['To']="dishant22@gmail.com"
msg['Subject']="hello"

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("dishantsethi@gmail.com","yourpassowrdhere")
server.send_message(msg)
print("mail sent")
server.quit()

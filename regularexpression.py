import re
s="take  5 one  1-13-2020 idea .one idea 2  5 at a time"
#result=re.search(r'o\w\w',s)                #\w means any character means after o any two characters
#print(result.group())                      #re.search shows only first one
result=re.findall(r'o\w\w',s)               #re.findall will shoe every ehich starts with this
print(result)

res=re.match(r't\w\w\w',s)      #only search at starting
print(res.group())                  #\w+ means one or more   \w* 0 or more

resu=re.split(r'\d+',s)     #d means digits
print(resu)                     #\w{1} means one only   \w{1,3} means one to three

#res1=re.sub(r'one','two',s)                   #replace
#print(res1)

res1=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',s)         #for dates
print(res1)

                #special character

res2=re.search(r'^t\w*',s)                #^ means at the starting
print(res2.group())

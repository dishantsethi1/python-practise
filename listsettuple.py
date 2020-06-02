lst=[10,20,'dishant']
#print(lst)

lst.append(40)
lst.remove('dishant')
del(lst[1])
#print(lst)

#lst.clear()
#print(lst)
#(max(lst))
#print(min(lst))
lst.insert(2,30)
#print(lst)

lst.sort(reverse=True)
#print(lst)


            #tuple
tpl=(40,50,'dis')                               #if one is there always use comma after it tpl=(39,)     cant change
#print(tpl)
#print(tpl.count(40))
#print(tpl.index('dis'))

tpl1=tuple(lst)
#print(tpl1)


            #set no duplicates

s={10,20,30,'dis'}

print(type(s))                          #tocheck type

s.update([88,90])
s.remove(88)
        #print(s)                   #set doesnot support indexing,slicing



                #frozen set

f=frozenset(s)                      #cant update  or remove




                #rangetype

r=range(5)                          #stars from zero
#for i in r :
    #print(i)

e=range(1,15,3)                     #step of 3
#for i in e:
    #print(i)


                #bytes
b=bytes(lst)                        #cant modify bytes
b1=bytearray(lst)
b1[2]=22


            #dictionary
dict={1:'dis',2:'sethi'}
#print(dict)
#print(dict.items())
k=dict.keys()
#for i in k: print(i)

v=dict.values()
#for i in v:print(i)

#print(dict[2])                         #by key
#del dict[1]
#print(dict)

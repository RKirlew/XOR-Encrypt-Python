key='K'
f=open("test.txt","rb")
q=""
q=f.read()
print(q)
omfg=""
t=open("test.txt","w")
for i in q:
        omfg+=chr(int(str(int(str(ord(chr(i)))) ^int((str(ord(str(key))))))))
f.close()
t.write(omfg)
t.close()

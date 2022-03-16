s=input()
a=[]
for i in s:
    a.append(int(i))
e=[]
o=[]
for i in a:
    if i%2==0:
        e.append(i)
    else:o.append(i)


for i in o:
    print(i,end='')
print(' ',end='')
for i in e:
    print(i,end='')

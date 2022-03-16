s=input()
s=list(s)
res=[]
for i in s:
    if i not in res:
        res.append(i)
print(''.join(res))

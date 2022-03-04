n=int(input('Enter a number: '))
a=[]
for i in range(n):
    a.append(int(input()))
res=[]
for j in range(n):
    for k in range(j+1,n):
        if a[j]==a[k]:
            if a[j] not in res:
                res.append(a[j])
print(len(res))

#program to subtract two matrices
a=[]
m=int(input('enter number of rows: '))
n=int(input('enter number of columns: '))
for i in range(m):
    row=[]
    for j in range(n):
        k=int(input())
        row.append(k)
    a.append(row)
for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j],end=' ')
    print()
b=[]
for i in range(m):
    row=[]
    for j in range(n):
        k=int(input())
        row.append(k)
    b.append(row)
for i in range(len(b)):
    for j in range(len(b[0])):
        print(b[i][j],end=' ')
    print()
result=[]
for i in range(m):
    row=[]
    for j in range(n):
        row.append(0)
    result.append(row)
for i in range(m):
    for j in range(n):
        result[i][j]=a[i][j]-b[i][j]
print('resultant matrix: ')
for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j],end=' ')
    print()

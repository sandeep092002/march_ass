#Assignment 2
s=input()
L=list(s)
l=0
u=0
d=0
s=0
for i in L:
    if i.islower():
        l+=1
    elif i.isupper():
        u+=1
    elif i.isdigit():
        d+=1
    else:
        s+=1
if l>0 and u>0 and d>0 and s>0:
    print("Your password is valid")
else:
    print("Your password is invalid")

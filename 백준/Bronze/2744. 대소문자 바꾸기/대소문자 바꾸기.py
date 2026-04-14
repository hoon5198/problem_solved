a=input()
b=[]
for i in a:
    if i.upper()==i:
        b.append(i.lower())
    else:
        b.append(i.upper())
for j in b:
    print(j,end='')
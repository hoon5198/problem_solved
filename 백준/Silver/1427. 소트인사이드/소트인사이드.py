n=input()
n_li=[]
for i in n:
    n_li.append(int(i))
n_li.sort(reverse=True)
for j in n_li:
    print(j,end='')
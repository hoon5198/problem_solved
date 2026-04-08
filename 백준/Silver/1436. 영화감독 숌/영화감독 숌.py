n=int(input())
jong=[]
i=0
while len(jong)<=10000:
    i+=1
    if '666' in str(i):
        jong.append(i)
print(jong[n-1])
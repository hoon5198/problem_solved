
a,b,v=map(int,input().split())
day=(v-b)/(a-b)
if (v-b)%(a-b)!=0:
    print(int(day)+1)
else:
    print(int(day))

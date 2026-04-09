import math as m
a,b,v=map(int,input().split())
day=int(m.ceil((v-b)/(a-b)))
print(day)
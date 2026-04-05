t=int(input())
for _ in range(t):
    h,w,n=map(int,input().split())
    q=n%h
    r=n//h
    if q==0:
        q=h
        r-=1
    print(q*100+r+1)

h, m = map(int, input().split())
m-=45
if m>=0:
    print(h,m)
else:
    m=60+m
    if h>0:
        h-=1
    else:
        h=23
    print(h,m)
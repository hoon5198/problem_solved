n,m=map(int, input().split())
a=[0 for _ in range(n)]
for _ in range(m):
    i,j,k=map(int, input().split())
    for l in range(i,j+1):
        a[l-1]=k
for h in range(n):
    print(a[h],end=" ")

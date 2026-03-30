n,m = map(int, input().split())
li = []
for k in range(1,n+1):
    li.append(k)
for i in range(m):
    a,b = map(int, input().split())
    li[a-1],li[b-1]=li[b-1],li[a-1]
for j in range(n):
    print(li[j],end=' ')

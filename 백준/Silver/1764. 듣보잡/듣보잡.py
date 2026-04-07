n, m=map(int,input().split())
nh=set(input() for _ in range(n))
ns=set(input() for _ in range(m))
nhs=list(nh&ns)
nhs.sort()
print(len(nhs))
for h in nhs:
    print(h)
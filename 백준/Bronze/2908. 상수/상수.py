a,b=map(list,input().split())
a[0],a[-1]=a[-1],a[0]
b[0],b[-1]=b[-1],b[0]
print("".join(max(a,b)))

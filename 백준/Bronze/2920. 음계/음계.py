a=list(map(int,input().split()))
if a==sorted(a):
    print('ascending')
elif sorted(a,reverse=True)==a:
    print('descending')
else:
    print('mixed')

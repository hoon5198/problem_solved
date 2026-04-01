n=int(input())
n_li=list(map(int,input().split()))
nn_li=[]
m=max(n_li)
for i in range(n):
    nn_li.append(n_li[i]/m*100)
print(sum(nn_li)/n)
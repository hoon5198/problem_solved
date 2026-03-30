n = int(input())
n_list = list(map(int, input().split()))
v = int(input())
count = 0
for i in range(n):
    if v==n_list[i]:
        count+=1
print(count)



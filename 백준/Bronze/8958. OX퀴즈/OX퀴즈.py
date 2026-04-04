t=int(input())

for i in range(t):
    s=input()
    count=0
    sum_count=0
    for j in s:
        if j=='O':
            count+=1
        else:
            count=0
        sum_count+=count
            
    print(sum_count)



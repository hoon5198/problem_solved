aa = []
for i in range(9):
    a = int(input())
    aa.append(a)
print(max(aa))
print(aa.index(max(aa))+1)
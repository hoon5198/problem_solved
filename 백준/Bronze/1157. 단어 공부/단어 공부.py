word=input().lower()
w=[]
count_list=[]
c=0
for i in word:
    if i not in w:
        w.append(i)
for i in w:
    count_list.append([i,word.count(i)])
m=max(count_list,key=lambda x:x[1])
for j in count_list:
    if m[1]==j[1]:
        c+=1
if c>1:
    print('?')
else:
    print(m[0].upper())
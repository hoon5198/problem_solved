count=0
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input())
a=str(factorial(n))
for i in range(1,len(a)+1):
    if a[-i]=='0':
        count+=1
    else:
        break
print(count)
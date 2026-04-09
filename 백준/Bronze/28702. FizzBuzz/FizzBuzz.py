b=0
a_li=[input() for _ in range(3)]
if a_li[2].isdigit():
    b=int(a_li[2])+1
elif a_li[1].isdigit():
    b=int(a_li[1])+2
elif a_li[0].isdigit():
    b=int(a_li[0])+3

if b%3==0 and b%5==0:
    print("FizzBuzz")
elif b%3==0 and b%5!=0:
    print("Fizz")
elif b%3!=0 and b%5==0:
    print("Buzz")
else:
    print(b)
        
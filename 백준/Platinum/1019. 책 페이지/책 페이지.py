import sys

def calc(n, point, ans):
    # 숫자를 각 자릿수별로 분리해서 개수를 더해주는 함수
    while n > 0:
        ans[n % 10] += point
        n //= 10

def solve():
    n = int(sys.stdin.readline())
    ans = [0] * 10
    
    start = 1
    end = n
    point = 1 # 자릿수 (1, 10, 100, ...)

    while start <= end:
        # start의 일의 자리가 0이 될 때까지 증가시키며 개수 직접 세기
        while start % 10 != 0 and start <= end:
            calc(start, point, ans)
            start += 1
        
        # start가 end보다 커지면 종료
        if start > end:
            break
            
        # end의 일의 자리가 9가 될 때까지 감소시키며 개수 직접 세기
        while end % 10 != 9 and start <= end:
            calc(end, point, ans)
            end -= 1
            
        # 이제 start의 일의 자리는 0, end의 일의 자리는 9
        # 이 사이의 숫자들은 0~9가 균등하게 등장함
        cnt = (end // 10 - start // 10 + 1)
        for i in range(10):
            ans[i] += cnt * point
            
        # 다음 자릿수(10의 자리, 100의 자리...)로 이동
        start //= 10
        end //= 10
        point *= 10

    print(' '.join(map(str, ans)))

solve()
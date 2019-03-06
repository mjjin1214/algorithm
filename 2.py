import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    Data = list(map(int, input().split()))
    max_mul = 0
    for i in range(N-1):
        for j in range(i+1, N):
            mul = Data[i] * Data[j]
            temp = mul
            while temp // 10:
                a = temp % 10
                temp //= 10
                if a < (temp % 10):
                    break
            else:
                if max_mul < mul:
                    max_mul = mul

    if max_mul:
        answer = max_mul
    else:
        answer = -1

    print('#{} {}'.format(t+1, answer))

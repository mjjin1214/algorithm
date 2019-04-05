import sys
sys.stdin = open('input2.txt')


def GCD(a, b):
    if abs(a) < abs(b):
        return GCD(b, a)
    elif b == 0:
        return a
    else:
        return GCD(b, a%b)


T = int(input())
for t in range(T):
    R, N, K = map(int, input().split())
    data = [() for _ in range(N)]
    for n in range(N):
        data[n] = tuple(map(int, input().split()))

    answer = 0
    for i in range(len(data)):
        temp_set = set()
        for j in range(len(data)):
            if i == j:
                continue
            a = data[j][0]-data[i][0]
            b = data[j][1]-data[i][1]
            if a == 0:
                b //= abs(b)
            elif b == 0:
                a //= abs(a)
            else:
                c = GCD(a, b)
                a //= c
                b //= c
            temp_set.add((a, b))
        print(temp_set)
        answer += len(temp_set)
    print('#{} {}'.format(t+1, answer))

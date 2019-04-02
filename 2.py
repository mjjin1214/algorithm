import sys
sys.stdin = open('input2.txt')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    data = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        data[a][b] = 1
        data[b][a] = 1

    answer = [0]*(N+1)
    for i in range(2, N+1):
        if data[1][i]:
            answer[i] = 1
            for j in range(2, N+1):
                if data[i][j]:
                    answer[j] = 1

    print('#{} {}'.format(t+1, answer.count(1)))

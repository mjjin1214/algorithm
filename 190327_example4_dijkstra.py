import sys
sys.stdin = open('input2.txt')


def answer(x):
    if x == 0:
        print('rout : 0', end=' ')
        return
    answer(vector[x][1])
    print(x, end=' ')
    return


N, L = map(int, input().split())
matrix = [[99 for _ in range(N)] for _ in range(N)]
for l in range(L):
    data = list(map(int, input().split()))
    matrix[data[0]][data[1]] = data[2]

vector = [[0, 0] for _ in range(N)]
for k in range(N):
    vector[k][0] = matrix[0][k]
    vector[k][1] = 0

visit = 0
whil = (1<<N)-1
visit ^= 1<<0
while visit < whil:
    min_vector = 999999999
    for j in range(N):
        if not visit & (1<<j):
            if min_vector > vector[j][0]:
                min_vector = vector[j][0]
                now = j

    visit ^= 1<<now
    for i in range(N):
        if vector[i][0] > vector[now][0] + matrix[now][i]:
            vector[i][0] = vector[now][0] + matrix[now][i]
            vector[i][1] = now

for m in range(N):
    print('distance : {}'.format(vector[m][0]), end=' / ')
    answer(m)
    print()
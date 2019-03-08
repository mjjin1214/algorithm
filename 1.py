import sys

sys.stdin = open('input.txt', 'r')


def safe(y, x):
    if 0 < y < 100 and 0 <= x < 100 and Data[y][x]:
        return True
    return False


def dfs(y, x):
    global count, min_count
    if min_count < count:
        return
    for j in range(3):
        if safe(y + dy[j], x + dx[j]):
            if j != 2:
                k = 1
                while safe(y + dy[j]*k, x + dx[j]*k):
                    count += 1
                    k += 1
                else:
                    dfs(y + dy[j]*k + 1, x + dx[j]*k)
                    break
            else:
                dfs(y + dy[j], x + dx[j])


dy = [0, 0, 1]
dx = [1, -1, 0]
for _ in range(10):
    t = int(input())
    Data = [0]*100
    for d in range(100):
        Data[d] = list(map(int, input().split()))

    min_count = 987654321
    for i in range(100):
        if Data[0][i] == 1:
            count = 0
            dfs(1, i)
            if min_count >= count:
                min_count = count
                min_index = i

    print('#{} {}'.format(t, min_index))

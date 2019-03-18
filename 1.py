import sys
sys.stdin = open('input.txt')


def sudoku():
    for i in range(9):
        Data[i] = list(map(int, input().split()))
        if len(set(Data[i])) != 9:
            for p in range(i+1, 9):
                Data[i] = input()
            return 0

    for m in range(1, 9, 3):
        for n in range(1, 9, 3):
            sum9 = Data[m][n]
            for o in range(8):
                sum9 += Data[m+dy[o]][n+dx[o]]
            if sum9 != 45:
                return 0

    for j in range(9):
        for k in range(j+1, 9):
            if k > j:
                Data[j][k], Data[k][j] = Data[k][j], Data[j][k]

    for l in range(9):
        if len(set(Data[l])) != 9:
            return 0

    return 1


dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
T = int(input())
Data = [[] for _ in range(9)]
for t in range(T):
    print('#{} {}'.format(t+1, sudoku()))

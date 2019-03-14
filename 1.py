import sys
sys.stdin = open('input.txt')


def sudoku():
    for i in range(9):
        Data[i] = list(map(int, input().split()))
        if len(set(Data[i])) != 9:
            return 0

    for j in range(9):
        for k in range(9):
            if j > k:
                Data[j][k], Data[k][j] = Data[k][j], Data[j][k]

    for i in range(9):
        if len(set(Data[i])) != 9:
            return 0


T = int(input())
Data = [[] for _ in range(9)]
for t in range(T):
    print('#{} {}'.format(t+1, sudoku()))

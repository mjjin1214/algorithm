import sys
sys.stdin = open('input.txt', 'r')


def IsSafe(y, x):
    if 0 <= x < 5 and 0 <= y < 5:
        return True
    else:
        return False


def Mycalc(a, b):
    if a > b:
        return a-b
    else : return b-a


data = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    data[i] = list(map(int, input().split()))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

sum = 0
for y in range(5):
    for x in range(5):
        for dir in range(4):
            newY = y + dy[dir]
            newX = x + dx[dir]
            if IsSafe(newY, newX):
                sum += Mycalc(data[y][x], data[newY][newX])

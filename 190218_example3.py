# import sys
#
# sys.stdin = open('input.txt', 'r')
#
# data = list(map(int, input().split()))

data = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14]
]

length = len(data)
selection_l = []
for _ in range(length ** 2):
    min = length ** 2
    for y in range(length):
        for x in range(len(data[y])):
            if data[y][x] <= min:
                min = data[y][x]
                Y, X = y, x
    selection_l.append(min)
    data[Y][X] = length ** 2 + 1

print(selection_l)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

array_l = [[0 for _ in range(length)] for _ in range(length)]
print(array_l)

i,j, delta = 0, 0, 0
for num in selection_l:
    array_l[i][j] = num
    if j + dx[delta % 4] >= length or i + dy[delta % 4] >= length or array_l[i + dy[delta % 4]][j + dx[delta % 4]] != 0:
        delta += 1
    j += dx[delta % 4]
    i += dy[delta % 4]
    print(i, j, delta)

print(array_l)

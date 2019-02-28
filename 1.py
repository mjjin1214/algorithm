import sys

sys.stdin = open('input.txt', 'r')

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


# def dfs(y, x):
#     for i in range(8):
#         if 0 <= y+dy[i] < 19 and 0 <= x+dx[i] < 19:
#             if Data[y+dy[i]][x+dx[i]] == 1:
#                 ddy = ddx = 0
#                 while Data[y+dy[i]+ddy][x+dx[i]+ddx] == 1:

def right():
    for y in range(19):
        count = 0
        state = 0
        for x in range(19):
            if Data[y][x] != 0:
                if state != Data[y][x]:
                    if count == 5:
                        return state, y+1, x - 4
                    state = Data[y][x]
                    count = 1
                else:
                    count += 1
            else:
                if count == 5:
                    return state, y+1, x - 4
                else:
                    count = 0
                    state = 0
        else:
            if count == 5:
                return state, y + 1, x - 4

def down():
    for x in range(19):
        count = 0
        state = 0
        for y in range(19):
            if Data[y][x] != 0:
                if state != Data[y][x]:
                    if count == 5:
                        return state, y - 4, x + 1
                    state = Data[y][x]
                    count = 1
                else:
                    count += 1
            else:
                if count == 5:
                    return state, y - 4, x + 1
                else:
                    count = 0
                    state = 0
        else:
            if count == 5:
                return state, y - 4, x + 1


def rightdown():
    for y in range(19-4):
        x = 0
        count = 0
        state = 0
        while y < 19:
            if Data[y][x] != 0:
                if state != Data[y][x]:
                    if count == 5:
                        return state, y - 4, x - 4
                    state = Data[y][x]
                    count = 1
                else:
                    count += 1
            else:
                if count == 5:
                    return state, y - 4, x - 4
                else:
                    count = 0
                    state = 0
            y += dy[3]
            x += dx[3]
        else:
            if count == 5:
                return state, y - 4, x - 4

    for x in range(1, 19-4):
        y = 0
        count = 0
        state = 0
        while x < 19:
            if Data[y][x] != 0:
                if state != Data[y][x]:
                    if count == 5:
                        return state, y - 4, x - 4
                    state = Data[y][x]
                    count = 1
                else:
                    count += 1
            else:
                if count == 5:
                    return state, y - 4, x - 4
                else:
                    count = 0
                    state = 0
            y += dy[3]
            x += dx[3]
        else:
            if count == 5:
                return state, y - 4, x - 4


def rightup():
    for y in range(5, 19):
        x = 0
        count = 0
        state = 0
        while y < 0:
            if Data[y][x] != 0:
                if state != Data[y][x]:
                    if count == 5:
                        return state, y + 4, x - 4
                    state = Data[y][x]
                    count = 1
                else:
                    count += 1
            else:
                if count == 5:
                    return state, y + 4, x - 4
                else:
                    count = 0
                    state = 0
            y += dy[1]
            x += dx[1]
        else:
            if count == 5:
                return state, y + 4, x - 4

    for x in range(1, 19 - 4):
        y = 18
        count = 0
        state = 0
        while x < 19:
            if Data[y][x] != 0:
                if state != Data[y][x]:
                    if count == 5:
                        return state, y + 4, x - 4
                    state = Data[y][x]
                    count = 1
                else:
                    count += 1
            else:
                if count == 5:
                    return state, y + 4, x - 4
                else:
                    count = 0
                    state = 0
            y += dy[1]
            x += dx[1]
        else:
            if count == 5:
                return state, y + 4, x - 4


Data = []
for _ in range(19):
    data = list(map(int, input().split()))
    Data.append(data)

for i in (right(), down(), rightdown(), rightup()):
    if i:

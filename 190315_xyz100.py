import sys
sys.stdin = open('input.txt')


def baek(a, b, c):
    global count2
    if c < b or b < a:
        return
    if a + b + c > 100:
        return
    if a + b + c == 100:
        count2 += 1
        return
    if tensor[a+1][b][c] == 0:
        tensor[a+1][b][c] = 1
        baek(a+1, b, c)
    if tensor[a][b+1][c] == 0:
        tensor[a][b+1][c] = 1
        baek(a, b+1, c)
    if tensor[a][b][c+1] == 0:
        tensor[a][b][c+1] = 1
        baek(a, b, c+1)


count = 0
count2= 0
tensor = [[[0 for _ in range(99)] for _ in range(99)] for _ in range(99)]
for i in range(1, 99):
    for j in range(i, 99):
        for k in range(j, 99):
            if i + j + k == 100:
                count += 1

print(count)

baek(1, 1, 1)

print(count2)

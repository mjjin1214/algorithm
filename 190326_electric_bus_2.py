import sys
sys.stdin = open('input1.txt')


def backtrack(x, count):
    global min_count
    if count >= min_count:
        return
    if x >= data[0]:
        if min_count > count:
            min_count = count
        return
    for i in range(data[x], 0, -1):
        backtrack(x+i, count+1)


T = int(input())
for t in range(T):
    data = list(map(int, input().split()))
    min_count = data[0]
    backtrack(1, 0)

    print('#{} {}'.format(t+1, min_count-1))
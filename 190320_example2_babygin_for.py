import sys
sys.stdin = open('input2.txt')


def rt(x):
    if x[0]+1 == x[1]:
        if x[1]+1 == x[2]:
            return True
    if x[0] == x[1]:
        if x[1] == x[2]:
            return True
    return False


def babygin():
    for i in range(6):
        for j in range(6):
            if i == j:
                continue
            for k in range(6):
                if i == k or j == k:
                    continue
                for l in range(6):
                    if i == l or j == l or k == l:
                        continue
                    for m in range(6):
                        if i == m or j == m or k == m or l == m:
                            continue
                        for n in range(6):
                            if i == n or i == n or k == n or l == n or m == n:
                                continue
                            x = [data[i], data[j], data[k]]
                            y = [data[l], data[m], data[n]]
                            if rt(x) and rt(y):
                                return print('baby gin')
    print('not baby gin')


data = list(map(int, input().split()))
babygin()

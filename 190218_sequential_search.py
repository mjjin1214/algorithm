import sys

sys.stdin = open('input.txt', 'r')

data = list(map(int, input().split()))


def sequential(list_x, x):
    for i in range(len(data)):
       if list_x[i] == x:
           return i
    else:
        return 'not exist'


print(sequential(data, 1))
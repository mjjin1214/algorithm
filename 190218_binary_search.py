import sys

sys.stdin = open('input.txt', 'r')

data = list(map(int, input().split()))


def binary(list_x, x):
    start, end = 0, len(list_x)-1
    while end < start:
        mid = (start + end) // 2
        if list_x[mid] == x:
            return mid
        else:
            if list_x[mid] > x:
                end = mid-1
            else:
                start = mid+1

    return 'not exist'


print(binary(data, 2))
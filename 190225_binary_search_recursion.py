import sys

sys.stdin = open('input.txt', 'r')

data = list(map(int, input().split()))


def binary(start, end, goal):
    if start > end:
        return False
    mid = (start + end) // 2
    if mid == goal:
        return True
    elif mid > goal:
        return binary(start, mid-1, goal)
    else:
        return binary(mid+1, end, goal)


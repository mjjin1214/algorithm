import sys

sys.stdin = open('input.txt', 'r')

data = list(map(int, input().split()))
matrix = [[0 for _ in range(max(data)+1)] for _ in range(max(data)+1)]
visited = [0]*(max(data)+1)
stack = [0]*len(data)
top = -1


def push(x):
    global top
    top += 1
    stack[top] = x


def pop():
    global top
    if top == -1:
        return 0
    x = stack[top]
    top -= 1
    return x


def findnext(here):
    for next in range(8):
        if matrix[here][next] and not visited[next]:
            return next


def dfs(here):
    global top
    print(here)
    visited[here] = True
    while here:
        next = findnext(here)
        if next:
            push(here)
        while next:
            here = next
            print(here)
            visited[here] = True
            next = findnext(here)
            push(here)
        here = pop()

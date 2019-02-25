import sys

sys.stdin = open('input.txt', 'r')


def backtrack(x, cost):
    global n, min_cost
    if x == n or min_cost < cost:
        if min_cost > cost:
            min_cost = cost
        return
    for i in range(1, n+1):
        if matrix[x][i]:
            visit_matrix[x][i] = 0
            backtrack(i, cost + matrix[x][i])
            visit_matrix[x][i] = 1


n, m = map(int, input().split())
matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
visit_matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in  range(m):
    a, b, w = map(int, input().split())
    matrix[a][b] = w
    matrix[b][a] = w
    visit_matrix[a][b] = 1

min_cost = 200*n
backtrack(1, 0)
if min_cost == 200*n:
    min_cost = -1
print(min_cost)

import sys

sys.stdin = open('input.txt', 'r')

data = list(map(int, input().split()))


# def DFS(here):
#     print(here)
#     visited[here] = True
#
#     for next in range(8):
#         if MyMap[here][next] and not visited[next]:
#             DFS(next)


def dfs(y):
    if check_list[y] == 1:
        return
    print(y)
    check_list[y] = 1
    for x in range(len(matrix[y])):
        if matrix[y][x] == 1:
            dfs(x)
    return


check_list = [0]*(max(data)+1)
matrix = [[0 for _ in range(max(data)+1)] for _ in range(max(data)+1)]
for i in range(0, len(data), 2):
    matrix[data[i]][data[i+1]] = matrix[data[i+1]][data[i]] = 1

print(data)
print(matrix)
print(dfs(1))

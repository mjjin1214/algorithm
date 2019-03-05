import sys

sys.stdin = open('input.txt', 'r')


def preorder(x):
    if x:
        print(x, end=' ')
        preorder(matrix[x][0])
        preorder(matrix[x][1])


def inorder(x):
    if x:
        inorder(matrix[x][0])
        print(x, end=' ')
        inorder(matrix[x][1])


def postorder(x):
    if x:
        postorder(matrix[x][0])
        postorder(matrix[x][1])
        print(x, end=' ')


def parents(x):
    x = matrix[x][3]
    if x:
        print(x, end=' ')
        parents(x)


def distance(x, y):
    queue.append(x)
    vector[x] = 1
    while queue:
        now = queue.pop(0)
        for i in (0, 1, 3):
            if matrix[now][i] == y:
                return print(vector[now])
            if matrix[now][i] and vector[matrix[now][i]] == 0:
                queue.append(matrix[now][i])
                vector[matrix[now][i]] = vector[now] + 1


node = int(input())
edges = list(map(int, input().split()))
matrix = [[0 for _ in range(5)] for _ in range(node+1)]
for i in range(0, (node-1)*2, 2):
    if matrix[edges[i]][0]:
        matrix[edges[i]][1] = edges[i+1]
    else:
        matrix[edges[i]][0] = edges[i+1]

    matrix[edges[i]][2] += 1
    matrix[edges[i+1]][3] = edges[i]
    matrix[edges[i+1]][4] = matrix[edges[i]][4] + 1

queue = []
vector = [0]*(node+1)
preorder(1)
print()
inorder(1)
print()
postorder(1)
print()
parents(13)
print()
distance(12, 13)
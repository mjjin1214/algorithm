import sys
sys.stdin = open('input1.txt')


def pre(i, p):
    if p[1]-p[0] < 0:
        return
    print(postorder[p[1]], end=' ')
    if i[1] == i[0] or p[1] == p[0]:
        return
    for j in range(len(inorder)):
        if inorder[j] == postorder[p[1]]:
            pre((i[0], j-1), (p[0], j-1))
            pre((j+1, i[1]), (j, p[1]-1))
            break

n = int(input())
inorder = input().split()
postorder = input().split()
visit = 0
pre((0, len(inorder)-1), (0, len(postorder)-1))
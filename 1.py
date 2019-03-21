import sys
sys.stdin = open('input1.txt')


def sor(i):
    for j in range(1, i+1):
        if j*2 <= i and tree[j] < tree[j * 2]:
            tree[j], tree[j * 2] = tree[j * 2], tree[j]
            sor(i)
            return
        if j*2+1 <= i and tree[j] > tree[j * 2 + 1]:
            tree[j], tree[j * 2 + 1] = tree[j * 2 + 1], tree[j]
            sor(i)
            return


T = int(input())
for t in range(T):
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    tree[0] = N + 1
    for i in range(1, N + 1):
        tree[i] = i
        sor(i)

    print(tree)

    print('#{} {} {}'.format(t + 1, tree[1], tree[N // 2]))

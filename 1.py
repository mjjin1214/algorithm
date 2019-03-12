import sys

sys.stdin = open('input.txt', 'r')


class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


def enqueue(item):
    global head2, tail2
    if head2 == None:
        head2 = Node(item)
        head2.left = head2.right = head2
        tail2 = head2
    else:
        p = tail2
        p.right = Node(item, p, head2)
        tail2 = p.right
        head2.left = tail2


def insertion():
    global head, head2, tail, tail2, N
    if head == None:
        head = head2
        tail = tail2
    elif head.data > head2.data:
        tail2.right = head
        tail2.right.left = tail2
        head = head2
    else:
        p = head
        while p.right:
            if p.right.data > head2.data:
                break
            p = p.right
        else:
            p.right = head2
            p.right.left = p
            tail = tail2

            return

        tail2.right = p.right
        p.right.left = tail2
        p.right = head2
        p.right.left = p


T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    head = None
    tail = None
    head2 = None
    tail2 = None
    data = list(map(int, input().split()))
    for d in data:
        enqueue(d)

    p = head2
    for _ in range(K):
        for _ in range(M-1):
            p = p.right

        p.right = Node(p.data+p.right.data, p, p.right)

    p = head2
    print('#{}'.format(t + 1), end=' ')
    for _ in range(10):
        p = p.left
        print(p.data, end=' ')
        if p.left == head2:
            break

    print()

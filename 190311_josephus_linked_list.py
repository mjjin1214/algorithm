class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link


def enqueue(item):
    global head
    newNode = Node(item)
    if head == None:
        head = newNode
        head.link = head
    else:
        p = head
        while p.link != head:
            p = p.link

        p.link = newNode
        newNode.link = head


def josephus(N, n, head):
    p = head
    while p.link.link!=p:
        p.link.link = p.link.link.link
        p = p.link.link

    q = p
    while q.link != p:
        print(q.data)
        q = q.link

    print(q.data)


head = None
for i in range(1, 42):
    enqueue(i)

josephus(41, 2, head)

class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link


def enqueue(item):
    global head
    newNode = Node(item)
    if head == None:
        head = newNode
    else:
        p = head
        if p.link == None:
            p.link = newNode
            return
        while p.link.data < item:
            p = p.link
            if p.link == None:
                p.link = newNode
                return

        newNode.link = p.link
        p.link = newNode


head = None

enqueue(1)
enqueue(5)
enqueue(2)
enqueue(4)
enqueue(3)

p = head
while p:
    print(p.data)
    p = p.link

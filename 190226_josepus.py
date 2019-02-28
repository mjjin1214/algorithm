def enQueue(en):
    global rear, n
    rear += 1
    Queue.append(en)


def deQueue():
    global front, n
    front += 1
    return Queue[front]

n = 41
Queue = []
front = -1
rear = -1

for i in range(1, n+1):
    enQueue(i)

print(Queue, front, rear)

j = 1
while rear-front > 2:
    if j % 3:
        enQueue(deQueue())
    else:
        deQueue()
    j += 1
else:
    print(Queue[front+1:rear+1])
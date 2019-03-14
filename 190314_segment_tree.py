import sys
sys.stdin = open('input.txt')
IDT = [0] * (1<<5)

Data = list(map(int, input().split()))
howmany = len(Data)


def update(a, b):
    where = base + a - 1
    IDT[where] = b
    where >>= 1

    while where:
        IDT[where] = IDT[where*2] + IDT[where*2+1]
        where >>= 1


def RSQ(ffrom, to):
    ffrom = ffrom + base-1
    to = to + base -1

    sum = 0
    while ffrom < to:
        if ffrom & 1:
            sum += IDT[ffrom]
            ffrom += 1
        if not (to & 1):
            sum += IDT[to]
            to -= 1
        ffrom >>= 1
        to >>= 1

    if ffrom == to:
        sum += IDT[ffrom]

    print(sum)


base = 1
while base < howmany:
    base <<= 1

for now in range(base, howmany+base):
    IDT[now] = Data.pop(0)

for parent in range(base-1, 0, -1):
    IDT[parent] = IDT[parent*2] + IDT[parent*2+1]

update(3, 1)
print(IDT)
RSQ(3, 8)

import sys
sys.stdin = open('input1.txt')


def quick(p, r):
    print(data, p, r)
    if p >= r:
        return
    l = p
    while True:
        while l<r and data[p] > data[l]:
            l += 1

        while l<r and data[p] <= data[r]:
            r -= 1

        if l == r:
            data[p], data[l] = data[l], data[p]
            quick(p, l-1)
            quick(l+1, len(data)-1)
            return
        else:
            data[l], data[r] = data[r], data[l]


for _ in range(3):
    data = list(map(int, input().split()))
    quick(0, len(data)-1)
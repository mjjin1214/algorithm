import sys

sys.stdin = open('input.txt', 'r')

data = list(map(int, input().split()))

counts = [0]*(max(data)+1)
for i in data:
    counts[i] += 1

triplet = 0
run = 0
for k in range(2):
    for j in counts:
        if j >= 3:
            counts[j] -= 3
            triplet += 1

    for l in range(len(counts)-2):
        if counts[l] >= 1 and counts[l+1] >= 1 and counts[l+2] >= 1:
            counts[l] -= 1
            counts[l+1] -= 1
            counts[l+2] -= 1
            run += 1

if triplet + run == 2:
    print('baby-gin')
else:
    print('not baby-gin')

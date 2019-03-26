import sys
sys.stdin = open('input1.txt')

N, M = map(int, input().split())
data = [0 for _ in range(N)]
for n in range(N):
    data[n] = int(input())

data.sort()
l = 0
r = min(data)*M
min_m = r
while l <= r:
    m = (l+r)//2
    count = 0
    for d in data:
        if d > m:
            break
        count += m // d
        if count >= M:
            if min_m > m:
                min_m = m
            r = m - 1
            break
    else:
        l = m + 1

print(min_m)

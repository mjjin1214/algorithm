import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

Data = list(map(int, input().split()))

length = 0
for line in Data:
    length += 1

max = 0
for now in range(length):
    count = 0
    for next in range(now, length):
        if Data[now] > Data[next]:
            count += 1
    if count > max:
        max = count

print(max)
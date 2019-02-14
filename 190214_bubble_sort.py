import sys

sys.stdin = open('input.txt', 'r')

data = list(map(int, input().split()))

for i in range(len(data)-1):
    for j in range(len(data)-1-i):
        if data[j] > data[j+1]:
            data[j+1], data[j] = data[j], data[j+1]

print(data)

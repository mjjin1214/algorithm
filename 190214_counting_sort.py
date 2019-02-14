import sys

sys.stdin = open('input.txt', 'r')

data = list(map(int, input().split()))

counts = [0]*(max(data)+1)
for i in data:
    counts[i] += 1

for k in range(len(counts)-1):
    counts[k+1] += counts[k]

answer = [0]*(len(data))
for j in data:
    counts[j] -= 1
    answer[counts[j]] = j
    print(answer)

print(answer)
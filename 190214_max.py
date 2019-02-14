import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

Data = list(map(int, input().split()))
howmany = len(Data)
max = Data[0] #min = 0x7fffffff
maxindex = -1
for now in range(howmany):
    if max < Data[now]:
        max = Data[now]
        maxindex = now

print(max)
print(maxindex)
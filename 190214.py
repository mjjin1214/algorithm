import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

Data = list(map(int, input().split()))

print(Data)
import sys
sys.stdin = open('input2.txt')

def subset(k, su):
    if k == len(data):
        return
    if len(answer) > 0 and su == 0:
        return print(answer)
    subset(k+1, su)
    answer.append(data[k])
    subset(k+1, su+data[k])
    answer.pop(-1)

data = list(map(int, input().split()))
answer = []
subset(0, 0)
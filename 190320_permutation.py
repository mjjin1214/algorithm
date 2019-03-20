import sys
sys.stdin = open('input2.txt')

def backtrack(x):
    if x == len(data):
        return print(answer)
    for i in range(len(data)):
        if vector[i] == 0:
            vector[i] = 1
            answer[x] = data[i]
            backtrack(x+1)
            vector[i] = 0


def backtrack2(x):
    if x == len(data):
        return print(answer)
    for i in range(len(data)):
        answer[x] = data[i]
        backtrack2(x+1)


data = list(input().split())
vector = [0 for _ in range(len(data))]
answer = [0 for _ in range(len(data))]
backtrack(0)
backtrack2(0)

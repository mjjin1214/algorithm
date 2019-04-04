import sys
sys.stdin = open('input2.txt')


def subset(n, su):
    global visit, count
    if n == len(score):
        if not visit & (1<<su):
            visit ^= (1<<su)
            count += 1
        return
    subset(n+1, su+score[n])
    subset(n+1, su)


T = int(input())
for t in range(T):
    N = int(input())
    score = list(map(int, input().split()))
    vector = [0]*(sum(score)+1)
    score = list(set(score))
    for s in score:
        vector[s] = 1

    for i in range(len(vector)):
        if vector[i]:
            for j in range(len(vector)):
                vector[i+j] = 1

    # visit = count = 0
    # subset(1, score[0])
    print('#{} {}'.format(t+1, sum(vector)))

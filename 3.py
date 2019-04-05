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
    score = list(set(map(int, input().split())))
    visit = count = 0
    subset(0, 0)
    print('#{} {}'.format(t+1, count+N-len(score)))
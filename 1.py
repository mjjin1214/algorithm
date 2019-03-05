import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T):
    N, L, k = map(int, input().split())
    ID = []
    plus = []
    minus = []
    for _ in range(N):
        p, a = map(int, input().split())
        ID.append(a)
        if a > 0:
            plus.append(L-p)
            now = len(plus-1)
            pre = now - 1
            while plus[pre] > plus[now]:
                plus[pre], plus[now] = plus[now], pre[now]
                now = pre
                pre = now -1

        else:
            minus.append(p-0)
            if len(minus) > 2:
            now = len(plus - 1)
            pre = now - 1
            while plus[pre] > plus[now]:
                plus[pre], plus[now] = plus[now], pre[now]
                now = pre
                pre = now - 1
    K = 0
    while K < k:
        if not plus or plus[0] > minus[0]:
            answer = ID.pop(0)
            minus.pop(0)
            K += 1
        elif not minus or plus[0] < minus[0]:
            answer = ID.pop(-1)
            plus.pop(0)
            K += 1
        else:
            if abs(ID[0]) < abs(ID[-1]):
                answer = ID.pop(0)
                minus.pop(0)
            else:
                answer = ID.pop(-1)
                plus.pop(0)
            K += 1

    print(answer)

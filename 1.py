import sys

sys.stdin = open('input.txt', 'r')


def winner(a, b):
    if cards[a-1]-cards[b-1] == -1 or cards[a-1]-cards[b-1] == 2:
        return b
    else:
        return a


def divide(first, last):
    if last-first == 1:
        return winner(first, last)
    elif last-first == 0:
        return last
    return winner(divide(first, (first+last)//2), divide((first+last)//2+1, last))


T = int(input())
for t in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    print(f'#{t+1} {divide(1, N)}')

import sys

sys.stdin = open('input.txt', 'r')


def dfs(money):
    global B, n, max_money
    if money > B:
        return

    if money > max_money:
        max_money = money

    for i in range(n):
        if vector[i] == 0:
            vector[i] = 1
            dfs(money + data[i])
            vector[i] = 0



B = int(input())
n = int(input())
data = list(map(int, input().split()))
vector = [0]*n
max_money = 0
dfs(0)
print(max_money)
import sys

sys.stdin = open('input.txt', 'r')


def backtrack(k, now, distance):
    global total_distance
    if  total_distance <= distance:
        return
    if k == N:
        distance += abs(Data[1][0] - now[0]) + abs(Data[1][1] - now[1])
        if total_distance > distance:
            total_distance = distance
        return
    for j in range(2, N+2):
        if not check[j]:
            check[j] = 1
            backtrack(k+1, Data[j], distance + abs(Data[j][0]-now[0]) + abs(Data[j][1]-now[1]))
            check[j] = 0


T = int(input())
for t in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    Data = []
    for i in range(0, len(data), 2):
        Data.append([data[i], data[i+1]])

    check = [0]*(N+2)
    total_distance = 100*(N+1)
    backtrack(0, Data[0], 0)
    print(f'#{t + 1} {total_distance}')

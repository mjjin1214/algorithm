import sys
sys.stdin = open('input1.txt')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    list_N = list(map(int, input().split()))
    list_N.sort()
    list_M = list(map(int, input().split()))
    count = 0
    for m in list_M:
        left = 0
        right = N - 1
        now = 0
        while left <= right:
            mid = (left + right) // 2
            if list_N[mid] == m:
                count += 1
                break
            elif list_N[mid] > m:
                right = mid - 1
                if now == -1:
                    break
                now = -1
            else:
                left = mid + 1
                if now == 1:
                    break
                now = 1

    print('#{} {}'.format(t+1, count))
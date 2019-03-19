import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1):
    N, M = map(int, input().split())
    cand = set()
    for _ in range(N):
        data = input()
        if int(data, 16):
            Data = [0 for _ in range(M*4)]
            for d in range(len(data)):
                for k in range(4):
                    if int(data[d], 16) & (1<<4-k):
                        Data[d*4+k] = 1

            i = len(Data)-1
            while i > 0:
                if Data[i] == 1:
                    j = i
                    while Data[j] == 1:
                        j -= 28
                        if j < 0:
                            break
                    else:
                        cand.update(Data[j:i+1])
                        print(cand)
                        i = j
                else:
                    i -= 1


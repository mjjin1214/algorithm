import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    N2 = list(map(int, input().split()))
    N_list = list(range(N))
    N_list_re = list(range(N-1, -1, -1))
    count = 0
    while N_list != N_list_re:
        for i in range(len(N_list)-1, 0, -1):
            if N_list[i] > N_list[i-1]:
                break

        for j in range(len(N_list)-1, i-1, -1):
            if N_list[j] > N_list[i-1]:
                N_list[j], N_list[i-1] = N_list[i-1], N_list[j]
                N_list[i:] = N_list[i:][::-1]
                break

        bolts = []
        for k in N_list:
            bolts += N2[k*2:k*2+2]

        temp = 0
        for l in range(1, len(bolts)-1, 2):
            if bolts[l] == bolts[l+1]:
                temp += 1
                if temp > count:
                    count = temp
                    max_bolts = bolts[:]
            else:
                temp = 0

    print(f"#{t+1} {' '.join(map(str, max_bolts))}")

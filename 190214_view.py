for i in range(10):
    num_case = int(input())
    case = list(map(int, input().split()))
    count = 0
    for j in range(2, num_case-2):
        if case[j-2] < case[j] and case[j-1] < case[j] and case[j] > case[j+1] and case[j] > case[j+2]:
            count += case[j] - max(case[j-2], case[j-1], case[j+1], case[j+2])

    print(f'#{i+1} {count}')
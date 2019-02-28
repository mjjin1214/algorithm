def subset(k, sum_set):
    if k > 9 or sum_set > 10:
        return
    if sum_set == 10:
        for l in range(10):
            if check[l]:
                answer.append(check[l])
    check[j] = 1
    subset(k+1, sum_set + data[j])
    check[j] = 0
    subset(k + 1, sum_set)


data = [i for i in range(1, 11)]
sum_set = 0
check = [0]*10
answer = []
subset(0, 0)

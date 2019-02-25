def subset(k):
    global sum_set
    if k > 9 or sum_set > 10:
        return
    for j in range(10):
        if not check[j]:
            sum_set += data[j]
            check[j] = 1
            answer.append(data[j])
            if sum_set == 10:
                print(answer)
            subset(k+1)
            sum_set -= data[j]
            check[j] = 0
            answer.pop(k)


data = [i for i in range(1, 11)]
sum_set = 0
check = [0]*10
answer = []
subset(0)

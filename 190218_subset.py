import sys

sys.stdin = open('input.txt', 'r')

data = list(map(int, input().split()))


def subset(data):
    subset_list = []
    for i in range(1 << (len(data))):
        temp = []
        for j in range(len(data)):
            if i & 1 << j:
                temp.append(data[j])
        if sum(temp) == 0:
            subset_list.append(temp)

    return subset_list


print(subset(data))

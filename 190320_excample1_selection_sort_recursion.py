import sys
sys.stdin = open('input2.txt')


def selection(index):
    if index == len(data):
        return
    min_v = 999999999
    for i in range(index, len(data)):
        if min_v > data[i]:
            min_v = data[i]
            min_i = i

    data[index], data[min_i] = data[min_i], data[index]
    selection(index+1)



data = list(map(int, input().split()))
selection(0)
print(data)

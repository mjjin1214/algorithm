import sys

sys.stdin = open('input.txt', 'r')

data = list(map(int, input().split()))

def next_permutation(data):
    for index in range(len(data)-1, -1, -1):
        if data[index] > data[index-1]:
            cand1 = index-1
            break
    else: return False

    for index in range(len(data)-1, cand1, -1):
        if data[index] > data[cand1]:
            data[index], data[cand1] = data[cand1], data[index]
            data[cand1+1:] = data[cand1+1:][::-1]
            break

    return data


print(next_permutation(data))

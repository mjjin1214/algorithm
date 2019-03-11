import sys
sys.stdin = open('input.txt', 'r')


def merge_sort(fro, to):
    if fro == to:
        return [data[fro], 1000000001]
    m = (fro + to) // 2
    left = merge_sort(fro, m)
    right = merge_sort(m+1, to)
    return merge(left, right)


def merge(left, right):
    global count
    result = [0]*(len(left)+len(right)-2)+[1000000001]
    l_i = 0
    r_i = 0
    result_i = 0
    while l_i < len(left)-1 or r_i < len(right)-1:
        if left[l_i] > right[r_i]:
            result[result_i] = right[r_i]
            result_i += 1
            r_i += 1
            count += len(left)-1-l_i
        else:
            result[result_i] = left[l_i]
            result_i += 1
            l_i += 1

    return result


data = list(map(int, input().split()))
count = 0
print(merge_sort(0, len(data)-1)[:-1])
print(count)
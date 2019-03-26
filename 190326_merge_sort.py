def div(a, z):
    if z-a <= 1:
        return (a, z)
    left = div(a, a+(z-a)//2)
    right = div(a+(z-a)//2, z)
    return merge(left, right)


def merge(left, right):
    global count
    temp_left = data[left[0]:left[1]]
    temp_right = data[right[0]:right[1]]
    l = 0
    r = 0
    if temp_left[-1] > temp_right[-1]:
        count +=1
    i = left[0]
    while i < right[1]:
        if l >= len(temp_left):
            data[i] = temp_right[r]
            r += 1
        elif r >= len(temp_right):
            data[i] = temp_left[l]
            l += 1
        elif temp_left[l] <= temp_right[r]:
            data[i] = temp_left[l]
            l += 1
        else:
            data[i] = temp_right[r]
            r += 1
        i += 1

    return (left[0], right[1])


T = int(input())
for t in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    count = 0
    div(0, N)
    print('#{} {} {}'.format(t+1, data[N//2], count))
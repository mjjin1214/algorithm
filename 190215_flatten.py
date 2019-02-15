for num_case in range(1, 11):
    dump = int(input())
    heights = list(map(int, input().split()))
    for num_dump in range(dump+1):
        max = 0
        min = 101
        for index_height, height in enumerate(heights):
            if height > max:
                max = height
                index_max = index_height
            if height < min:
                min = height
                index_min = index_height

        if max - min <= 1:
            break
        heights[index_max] -= 1
        heights[index_min] += 1

    print(f'#{num_case} {max-min}')

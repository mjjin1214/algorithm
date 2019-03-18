Data = [5, 1, -4, 2, -1, -5, -2, 8, -3, 6]
rangesum = [[Data[0], 0]]+[[0, 0] for _ in range(len(Data)-1)]
for i in range(1, len(rangesum)):
    if rangesum[i-1][0]+Data[i] > Data[i]:
        rangesum[i][0] = rangesum[i-1][0]+Data[i]
        rangesum[i][1] = rangesum[i-1][1]
    else:
        rangesum[i][0] = Data[i]
        rangesum[i][1] = i

max_sum = 0
for j in range(len(rangesum)):
    if max_sum < rangesum[j][0]:
        max_sum = rangesum[j][0]
        max_index = j

print(rangesum[max_index][0])
print(Data[rangesum[max_index][1]:max_index+1])

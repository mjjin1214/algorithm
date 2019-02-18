heights = []
for i in range(9):
    heights.append(int(input()))

heights.sort()

def answer(heights):
    seven = [0]*7
    for j in range(len(heights)):
        seven[0] = heights[j]
        for k in range(len(heights)):
            if j == k:
                continue
            seven[1] = heights[k]
            for l in range(len(heights)):
                if j == l or k == l:
                    continue
                seven[2] = heights[l]
                for m in range(len(heights)):
                    if j == m or k == m or l == m:
                        continue
                    seven[3] = heights[m]
                    for n in range(len(heights)):
                        if j == n or k == n or l == n or m == n:
                            continue
                        seven[4] = heights[n]
                        for o in range(len(heights)):
                            if j == o or k == o or l == o or m == o or n == o:
                                continue
                            seven[5] = heights[o]
                            for p in range(len(heights)):
                                if j == p or k == p or l == p or m == p or n == p or o == p:
                                    continue
                                seven[6] = heights[p]
                                sum = 0
                                for q in seven:
                                    sum += q
                                if sum == 100:
                                    return seven

print('\n'.join(map(str, answer(heights))))

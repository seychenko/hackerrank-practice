# Problem: https://www.hackerrank.com/challenges/2d-array/problem


def hourglassSum(arr):
    maximum = -63

    for i in range(4):
        for j in range(4):
            top_component = sum(arr[i][j:j+3])
            mid_component = arr[i+1][j+1]
            bot_component = sum(arr[i+2][j:j+3])
            hourglass_sum = top_component + mid_component + bot_component
            maximum = max(maximum, hourglass_sum)
    return maximum


arr = []
for _ in range(6):
    arr.append(list(map(int, input().split())))

result = hourglassSum(arr)
print(result)
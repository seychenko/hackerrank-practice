def rotateLeft(n, d, arr):
    arr.extend(arr)
    return arr[d:d+n]


n, d = map(int, input().split())
arr = list(map(int, input().split()))

result = rotateLeft(n, d, arr)
print(*result)
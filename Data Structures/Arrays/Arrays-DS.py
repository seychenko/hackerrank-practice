# Problem: https://www.hackerrank.com/challenges/arrays-ds/problem


def reverseArray(a):
    result = a[::-1]
    return result


arr_count = int(input())
arr = list(map(int, input().split()))
res = reverseArray(arr)
print(*res)
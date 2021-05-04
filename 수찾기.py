N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


def binary_search(num, arr, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if num == arr[mid]:
        return 1
    elif num < arr[mid]:
        return binary_search(num, arr, start, mid - 1)
    else:
        return binary_search(num, arr, mid + 1, end)


A.sort()
for num in B:
    start = 0
    end = N - 1
    print(binary_search(num, A, start, end))

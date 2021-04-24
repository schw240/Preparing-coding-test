N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


def binary_search(num, A, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if num == A[mid]:
        return 1
    elif num < A[mid]:
        return binary_search(num, A, start, mid - 1)
    else:
        return binary_search(num, A, mid+1, end)


A.sort()
for num in B:
    start = 0
    end = N - 1
    print(binary_search(num, A, start, end))

# 매장에 N개 부품, 정수형태의 고유한 번호
# 손님이 M개종류의 부품을 구매하겠다고함. 가게 안에 부품이 모두 있는지 확인하기

N = int(input())
arr1 = list(map(int, input().split(' ')))

M = int(input())
arr2 = list(map(int, input().split(' ')))

arr1.sort()
arr2.sort()


def binary_search(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if target == arr[mid]:
        return arr[mid]
    elif target < arr[mid]:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid + 1, end)


for i in arr2:
    res = binary_search(arr1, i, 0, N-1)

    if res != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

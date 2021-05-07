# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어있다.
# 이때 수열에서 x가 등장하는 횟수 계산
N, x = map(int, input().split(' '))
num_list = list(map(int, input().split(' ')))


def binary_search(num, arr, cnt, start, end):
    print(arr, "start arr")
    print(cnt, "start cnt")
    ans = cnt
    if start > end:
        return ans

    mid = (start + end) // 2

    if arr[mid] == num:
        cnt += 1
        arr.pop(mid)
        print(arr, "after pop")
        print(cnt, "after cnt")
        return binary_search(num, arr, cnt, start, end)
    elif arr[mid] >= num:
        return binary_search(num, arr, cnt, start, mid - 1)
    else:
        return binary_search(num, arr, cnt, mid + 1, end)


cnt = 0
cnt = binary_search(x, num_list, 0, cnt, len(num_list) - 1)
print(cnt, "마지막 cnt")
if cnt == 0:
    print(-1)
else:
    print(cnt)

# def count_by_value(arr, x):
#     n = len(arr)

#     # x가 처음 등장한 인덱스 계싼
#     a = first(arr, x, 0, n-1)

#     if a == None:
#         return 0

#     # x가 마지막으로 등장한 인덱스 계산
#     b = last(arr, x, 0, n-1)

#     # 개수
#     return b - a + 1

# # 처음 위치를 찾는 이진탐색


# def first(arr, target, start, end):
#     if start > end:
#         return None

#     mid = (start + end) // 2

#     # 해당 값을 가지는 원소중에서 왼쪽에 있는 경우에만 인덱스를 반환
#     if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target: # 찾는 값이고 mid가 0이거나, target이 arr[mid-1] 보다 클때
#         return mid
#     # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
#     elif arr[mid] >= target:
#         return first(arr, target, start, mid - 1)
#     # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
#     else:
#         return first(arr, target, mid + 1, end)


# def last(arr, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2

#     # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
#     if (mid == n-1 or target < arr[mid + 1]) and arr[mid] == target:
#         return mid
#     elif arr[mid] > target:
#         return last(arr, target, start, mid - 1)
#     else:
#         return last(arr, target, mid + 1, end)


# n, x = map(int, input().split())
# arr = list(map(int, input().split()))

# cnt = count_by_value(arr, x)

# if cnt == 0:
#     print(-1)
# else:
#     print(cnt)

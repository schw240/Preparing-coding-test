# 고정점이란 수열의 원소 중 그 값이 인덱스와 동일한 원소
# 하나의 수열이 N개의 서로 다른 원소를 포함 및 오름차순 정렬

def binary_search(arr, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    # 여기선 num이 idx랑 같은지 확인해야함 그럼 arr[mid] == mid
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return binary_search(arr, start, mid-1)
    else:
        return binary_search(arr, mid+1, end)


N = int(input())
num_list = list(map(int, input().split(' ')))
idx = binary_search(num_list, 0, N-1)

print(idx)

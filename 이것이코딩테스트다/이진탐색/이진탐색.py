# 배열 내부의 데이터가 정렬되어있어야만 사용할 수 있는 알고리즘
# 탐색 범위를 절반씩 좁혀가면서 데이터를 탐색하는 특징
# 시작점, 끝점, 그리고 중간점 3개의 변수를 이용하여 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복해서 비교한 다음 원하는 데이터 탐색
# 탐색하는 원소의 개수가 절반씩 줄어든 다는 점에서 시간 복잡도는 O(logN)

def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid

    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른 쪽 값 확인
    else:
        return binary_search(arr, target, mid + 1, end)

"""
퀵정렬이란?

- 기준점(pivot이라고 부름)을 정해서 기준점보다 작은 데이터는 왼쪽, 큰 데이터는 오른쪽으로 모으는 함수작성
- 각 왼쪽, 오른쪽은 재귀용법을 사용해서 다시 동일 함수를 호출하여 위 작업을 반복함
- 함수는 왼쪽 + 기준점 + 오른쪽을 리턴
"""


import random


def quicksort(data):
    if len(data) <= 1:
        return data

    left, right = list(), list()
    pivot = data[0]

    for i in range(1, len(data)):
        if data[i] > pivot:
            right.append(data[i])
        else:
            left.append(data[i])
    return quicksort(left) + [pivot] + quicksort(right)


# list comprehension 기법
def qsort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return qsort(left) + [pivot] + qsort(right)


data_list = random.sample(range(100), 10)

# print(quicksort(data_list))
print(qsort(data_list))

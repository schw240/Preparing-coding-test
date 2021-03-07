# 선택정렬
# 아래와 같은 순서를 반복하며 정렬하는 알고리즘
# 1. 주어진 데이터 중 최소값을 찾음
# 2. 해당 최소값을 데이터 맨 앞에 위치한 값과 교체함
# 3. 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복함


import random


def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand + 1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[stand] = data[stand], data[lowest]
    return data


data_list = random.sample(range(100), 10)
print(selection_sort(data_list))

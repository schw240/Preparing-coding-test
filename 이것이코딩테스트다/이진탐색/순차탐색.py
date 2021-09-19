# 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 차례대로 하나씩 확인하는 방법
# 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용하는 방법
# 시간만 충분하다면 항상 원하는 원소를 찾아낼 수 있다는 장점이 있음
def sequential_search(n, target, array):
    for i in range(n):
        if array[n] == target:
            return i + 1


input_data = input().split()
n = int(input_data[0])
target = input_data[1]

array = input().split()

priont(sequential_search(n, target, array))

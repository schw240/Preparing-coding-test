# 특정 조건이 부합할 때만 사용가능
# 모든 데이터가 양의 정수인 경우
# 데이터 개수가 N, 데이터 중 최대값이 K일때
# 계수 정렬은 최악의 경우에도 O(N + K) 시간복잡도 보장
# 가장 큰 데이터와 가장 작은 데이터의 차이가 1백만을 넘지 않을 때 효과적으로 사용 가능

# 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다
# 초기 7 5 9 0 3 1 6 2 9 1 4 8 0 5 2
# 먼저 가장 큰 데이터와 가장 작은 데이터의 범위가 모두 담길 수 있도록 하나의 리스트 생성
# 우리가 정렬할 데이터의 범위는 0부터 9까지 이므로 리스트의 인덱스가 모든 범위를 포함할 수 있도록 한다
# 처음에는 리스트의 모든 데이터가 0이 되도록 초기화하고 크기가 10인 리스트 생성
# 그 다음 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시키면 계수 정렬이 완성된다.

nums = [0 for _ in range(10)]
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

for i in range(len(arr)):
    nums[arr[i]] += 1

# 결과적으로 리스트에는 각 데이터가 몇번 등장했는지 횟수 기록되고
# 각 데이터 안의 값을 확인해서 해당 숫자만큼 출력하면 됨
print(nums)

for i in range(len(nums)):
    for j in range(nums[i]):
        print(i, end=' ')

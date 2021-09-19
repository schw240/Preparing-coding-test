# 높이 H를 지정하면 떡을 한번에 절단한다.
# H보다 긴 떡은 H위의 부분이 잘릴것이고 낮은 부분은 잘리지 않는다.
# 손님이 요청한 길이가 M일때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최대값은?

# 떡의 개수 N과 길이 M
N, M = map(int, input().split())
arr = list(map(int, input().split(' ')))

# 파라매트릭서치 문제
# 최적화 문제를 결정 문제로 바꾸어 해결하는 기법
# 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에서 이용

start = 0
end = max(arr)

res = 0
while(start <= end):
    total = 0

    mid = (start + end) // 2

    for i in range(N):
        if arr[i] > mid:  # 떡이 mid 보다 큰경우만
            total += arr[i] - mid  # 각 떡에서 mid 이전까지 자른 크기 더해주기
    # print(total)
    if total < M:
        # 만약 mid보다 작다면 떡을 더 잘라야 하므로 mid 크기 줄이기
        end = mid - 1
    else:
        res = max(res, mid)

        start = mid + 1

print(res)

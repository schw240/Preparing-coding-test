def solution(N, stages):
    answer = []
    # 도달 O 클리어X 플레이어 수 / 스테이지어 도달한 플레이어 수
    # 전체 스테이지 개수 N
    # 사용자 현재 스테이지 배열 stages
    # 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호 return
    total_person = len(stages)
    miss_rates = []
    for i in range(1, N+1):
        fail = 0
        for stage in stages:
            if i >= stage:
                fail += 1
        if total_person == 0:
            fail = 0
        else:
            miss_rate = fail / total_person
        total_person -= fail
        miss_rates.append((miss_rate, i))

    miss_rates.sort(key=lambda x: x[0] - x[1], reverse=True)
    answer = [i[0] for i in miss_rates]
    print(answer)

    return answer

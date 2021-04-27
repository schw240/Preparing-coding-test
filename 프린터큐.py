test_case = int(input())

for i in range(test_case):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    queue = [(value, idx) for idx, value in enumerate(queue)]

    # print(queue)
    # 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
    # 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
    # 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다.
    # 그렇지 않다면 바로 인쇄를 한다
    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            # 바로 인쇄
            count += 1
            if queue[0][1] == M:
                print(count)
                break
            else:
                queue.pop(0)
        else:  # 나머지 중 현재 문서보다 중요도가 큰 문서가 있다면
            # 큐의 가장 뒤에 재배치
            queue.append(queue.pop(0))

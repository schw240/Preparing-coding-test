# 아이들의 캔디를 하나씩 확인
def check(N, candy):
    for i in range(N):
        # 만약 아이의 캔디중 홀수개가 있다면
        if candy[i] % 2 == 1:
            # 처음부터 사탕을 가진 경우 보충
            candy[i] += 1
    # set은 중복제거해줌 근데 len함수를 이용해 길이가 1이라고하면
    # set안의 모든 수가 같다는 의미
    return len(set(candy)) == 1


def teacher(N, candy):
    tmp_list = [0 for i in range(N)]
    for idx in range(N):
        if candy[idx] % 2:
            candy[idx] += 1
        # 오른쪽 친구의 사탕값은 내가 가진것의 절반
        candy[idx] = candy[idx] // 2
        tmp_list[(idx+1) % N] = candy[idx]//2

    for idx in range(N):
        candy[idx] += tmp_list[idx]

    return candy


def process():
    # 각 프로세스마다 아이의 수, 현재 아이들이 가지고있는 캔디 배열 받기
    N, candy = int(input()), list(map(int, input().split()))
    cnt = 0
    # check함수를 활용하여 현재 아이의 수와 캔디 배열을 체크
    while not check(N, candy):
        cnt += 1
        candy = teacher(N, candy)
    print(cnt)


# 맨 처음 입력받는 테스트케이스만큼 process 반복한다.
T = int(input())
for i in range(T):
    process()

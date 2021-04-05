def rotate(key):
    n = len(key)
    m = len(key[0])
    matrix = [[0] * n for i in range(m)]
    for i in range(n):
        for j in range(m):
            matrix[j][n - i - 1] = key[i][j]
    return matrix


def test(extended_lock):
    lock_length = len(extended_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if extended_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    # 열쇠의 돌기 부분을 자물쇠의 홈 부분에 맞게 채우면 열림
    # 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 영향X
    # 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야함
    # 얄쇠의 돌기와 자물쇠의 돌기가 만나서는 안됨
    # 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 열 수 있음
    # 0 은 홈, 1은 돌기
    # 키는 M, lock은 N M은 항상 N이하

    m, n = len(key), len(lock)

    # lock 크기 3배
    extended_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 가운대로 lock 넣기
    for i in range(n):
        for j in range(n):
            extended_lock[i+n][j+n] = lock[i][j]

    # 로테돌며 확인 360도니까 4번
    for i in range(4):
        for j in range(n * 2):
            for k in range(n * 2):
                # lock과 key 맞춰보기
                for x in range(m):
                    for y in range(m):
                        extended_lock[j+x][k+y] += key[x][y]
                # lock과 key 맞는지 테스트
                if test(extended_lock) == True:
                    return True

                # 열쇠 빼주기 이걸 몰랐네.. 빼주는거 생각하기 or deepcopy 사용
                for x in range(m):
                    for y in range(m):
                        extended_lock[j+x][k+y] -= key[x][y]
        # 열쇠 회전시키기
        key = rotate(key)
    return False

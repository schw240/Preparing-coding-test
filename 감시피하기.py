# 선생님이 존재하는 칸은 T
# 학생은 S
# 장애물은 O
# 3개의 장애물을 설치해 모든 학생들이 선생님의 감시를 피할 수 있도록함

# 감시를 피할 수 있으면 YES 아니면 NO
from itertools import combinations

N = int(input())
hallway = [input().split() for _ in range(N)]

empty_list = []
teacher_list = []
for i in range(N):
    for j in range(N):
        if hallway[i][j] == 'X':
            empty_list.append((i, j))
        elif hallway[i][j] == 'T':
            teacher_list.append((i, j))


def watch():
    for teacher in teacher_list:
        x, y = teacher
        # 상
        nx, ny = x, y
        while nx > 0:
            nx -= 1
            if hallway[nx][ny] == 'S':
                return False

            if hallway[nx][ny] == 'O':
                break
        # 하
        nx, ny = x, y
        while nx < N - 1:
            nx += 1
            if hallway[nx][ny] == 'S':
                return False
            if hallway[nx][ny] == 'O':
                break
        # 좌
        nx, ny = x, y
        while ny > 0:
            ny -= 1
            if hallway[nx][ny] == 'S':
                return False
            if hallway[nx][ny] == 'O':
                break
        # 우
        nx, ny = x, y
        while ny < N - 1:
            ny += 1
            if hallway[nx][ny] == 'S':
                return False
            if hallway[nx][ny] == 'O':
                break
    return True


# 벽 3개 뽑기
for walls in combinations(empty_list, 3):


    # 벽 세우기
    for wall in walls:
        x, y = wall
        hallway[x][y] = 'O'
    # 벽을 세우면 감시 시작
    # 감시하기
    if watch():
        print('YES')
        break
    # 감시에 성공하면 벽을 철거하고 다른벽 세우기
    # 벽 허물기
    for wall in walls:
        x, y = wall
        hallway[x][y] = 'X'
else:
    print('NO')

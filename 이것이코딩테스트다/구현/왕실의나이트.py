# 체스판 8X8
# L자 형태로 이동 그냥 나이트 이동하는 형태
# 나이트 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램 작성하기

cur_pos = input()
# a1
row = cur_pos[1]
col = cur_pos[0]
col = int(ord(col) - int(ord('a'))) + 1

cnt = 0

# 나이트가 갈수 있는 위치
ok = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (-1, -2), (1, 2), (1, -2)]

for o in ok:
    nr = int(row) + o[0]
    nc = col + o[1]

    if nr >= 1 and nc >= 1 and nr <= 8 and nc <= 8:
        cnt += 1

print(cnt)

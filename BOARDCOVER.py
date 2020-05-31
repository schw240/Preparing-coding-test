"""게임판 덮기 입출력

input

3
3 7
#.....#
#.....#
##...##
3 7
#.....#
#.....#
##..###
8 10
##########
#........#
#........#
#........#
#........#
#........#
#........#
##########

return

0
2
1514
"""

def ways(board):
    BLOCKS = [[(0, 0), (1, 0), (0, 1)],
              [(0, 0), (0, 1), (1, 1)],
              [(0, 0), (1, 0), (1, 1)],
              [(0, 0), (1, 0), (1, -1)],
             ]
    
    row, column = len(board), len(board[0])
    white = 0

    for r in range(row):
        for c in range(column):
            if board[r][c] == 0:
                white += 1
    if white % 3 != 0:
        return 0

    def block_set(board, r, c, block_type, delta):
        ok = True
        for i in range(3):
            new_r = r + BLOCKS[block_type][i][0]
            new_c = c + BLOCKS[block_type][i][1]
            if new_r < 0 or new_r >= row or new_c < 0 or new_c >= column:
                ok = False
            else:
                board[new_r][new_c] += delta
                if board[new_r][new_c] > 1:
                    ok = False
        return ok

    def cover(board):
        y, x = -1, -1
        for r in range(row):
            for c in range(column):
                if board[r][c] == 0:
                    y, x = r, c
                    break
            if y != -1:
                break

        if y == -1:
            return 1
        ret = 0
        for typ in range(4):
            if block_set(board, y, x, typ, 1):
                ret += cover(board)
            block_set(board, y, x, typ, -1)
        return ret
    return cover(board)


if __name__ == '__main__':
    #테스트 케이스의 수
    C = int(input())
    ans = []

    for _ in range(C):
        board = []
        #H줄에 각 W 글자로 게임판의 모양이 주어짐 #은 검은칸 , '.'은 흰칸
        H, W = (int(n) for n in input().split())
        for _ in range(H):
            board.append([(1 if c == '#' else 0) for c in list(input())])
        ans.append(ways(board))

    for n in ans:
        print(n)
    
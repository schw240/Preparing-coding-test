def solution(board, moves):
    answer = 0
    doll_lst = [0] #인덱스 에러 방지
    for move in moves:
        for j in range(len(board)):
            if board[j][move-1] != 0: #해당 열에 비어있지 않고 인형이 있다면
                doll_lst.append(board[j][move-1]) #doll_lst에다가 인형 넣기
                board[j][move-1] = 0 #해당 칸에 있던 인형은 빼냈으니 0으로 바꿔주기
                if len(doll_lst) > 2 and doll_lst[-1] == doll_lst[-2]: #맨뒤 2개 요소가 같다면
                    answer += 2
                    doll_lst.pop()
                    doll_lst.pop()
                break #크레인으로 인형을 하나 옮기면 다음 moves로 넘어가야함
    return answer

moves = [1,5,3,5,1,2,1,4]
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
#res = 4
print(solution(board, moves))
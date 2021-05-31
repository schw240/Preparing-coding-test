n = int(input())
# 출력할 배열 초기화 모두 *로 채워주고 빈칸이 들어갈부분은 밑에서바꿔준다.
list = [['*'] * n for i in range(n)]


def starprint(n, list):  #
    if n < 3:  # 1일때는 바로 내보내어 *이 출력하게만든다.
        return

    if n == 3:  # 3일때 빈칸은 직접 채워준다.
        list[1][1] = " "

    else:
        starprint(n//3, list)  # 재귀를 통해 이전리스트를 완성시키고 넘겨준다.
        for i in range(n // 3):  # 빈칸들이 일정한 패턴으로 늘어나는것을 이용한다.
            for j in range(n // 3):
                if list[i][j] == " ":  # 하나의 빈칸에서 파생되는 빈칸들
                    list[i][j+n//3] = " "
                    list[i][j + 2*n//3] = " "
                    list[i+n//3][j] = " "
                    list[i+n//3][j+2*n//3] = " "
                    list[i+2*n//3][j] = " "
                    list[i+2*n//3][j+n//3] = " "
                    list[i+2*n//3][j+2*n//3] = " "
        for i in range(n):  # 가운데 부분은 직접 비워줬다.
            for j in range(n):
                if n//3 <= i < n//3*2 and n//3 <= j < n//3*2:
                    list[i][j] = " "

        return list


starprint(n, list)  # 함수실행
for i in range(n):
    for j in range(n):
        print(list[i][j], end="")
    print()

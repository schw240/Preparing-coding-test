def solution(triangle):
    #점화식 
    #value[row][idx] += max(value[row-1][idx-1, value[row-1][idx]])
    for i in range(1, len(triangle)):
        for j in range(i+1):
            #왼쪽값인경우
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            #오른쪽값인경우
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    #마지막층의 최대값 출력
    return max(triangle[-1])

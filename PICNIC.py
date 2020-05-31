#students 남아있는 학생
#remainFriend: 짝이될수있는 친구의 리스트

def DFS(students, remainFriend):
    count = 0
    
    if (remainFriend == 0): #끝까지 탐색한 경우 종료
        return 1
 
    for i in range(students, n):
        if (visited[i] == False):
            for j in range(i + 1, n):
                if ((visited[j] == False) and (isFriend[i][j] == True)):
                    visited[i] = visited[j] = True
                    count += DFS(i, remainFriend - 2)
                    visited[i] = visited[j] = False
    
    return count
 
#테스트 케이스의 수 C
C = int(input())
 
for i in range(C):
    #학생의 수 n , 친구 쌍의 수 m
    n, m = map(int, input().split())
    visited = [False] * n
    isFriend = [[False] * n for j in range(n)]
    friendsList = list(map(int, input().split()))
 
    for k in range(0, len(friendsList), 2):
        isFriend[friendsList[k]][friendsList[k + 1]] = True
        isFriend[friendsList[k + 1]][friendsList[k]] = True
 
    print(DFS(0, n))
# 총 걸그룹 수 N , 맞혀야할 문제의 수 M
# 각 걸그룹마다 팀 이름, 인원 수 , 멤버 이름 입력
# 그 이후 M개의 퀴즈 입력
# 0이면 팀의 이름, 1이면 멤버의 이름
# 0이면 해당 팀에 속한 멤버 이름 사전순으로 출력
# 1이면 해당 멤버가 속한 팀의 이름 출력

N, M = map(int, input().split())

team_mem, mem_team = {}, {}

for i in range(N):
    teamName, memNum = input(), int(input())
    team_mem[teamName] = []
    for j in range(memNum):
        memName = input()
        team_mem[teamName].append(memName)
        mem_team[memName] = teamName

# print(team_mem)
# print(mem_team)

for i in range(M):
    name, q = input(), int(input())
    if q:
        print(mem_team[name])
    else:
        for mem in sorted(team_mem[name]):
            print(mem)

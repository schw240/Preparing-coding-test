"""시계맞추기

input

2
12 6 6 6 6 6 12 12 12 12 12 12 12 12 12 12 
12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6

return

2
9
"""
#'X'이면 연결 '.'이면 연결안됨
INF = 9999
SWITCHES = 10
CLOCKS = 16
LINKED = [
	"XXX.............",
    "...X...X.X.X....",
    "....X.....X...XX",
    "X...XXXX........",
    "......XXX.X.X...",
    "X.X...........XX",
    "...X..........XX",
    "....XX.X......XX",
    ".XXXXX..........",
    "...XXX...X...X..",
]

#모든 시계가 12시를 가르키고 있는지 확인
def are_aligned(clocks):
	for clock in clocks:
		if clock != 12:
			return False
	return True

#switch번 스위치를 누름
def push(clocks, switch):
	for clock in range(CLOCKS):
		if LINKED[switch][clock] == 'X':
			clocks[clock] += 3
			if clocks[clock] == 15:
				clocks[clock] = 3

#clocks: 현재 시계들의 상태
#switch: 이번에 누를 스위치의 번호
#clocks , switch가 주어질 때 남은 스위치들을 눌러서 clocks를 12시로 맞출 수 있는 최소 횟수 반환
#만약 불가능하다면 INF 반환
def solve(clocks, switch):
	if switch == SWITCHES:
		if are_aligned(clocks):
			return 0
		else:
			return INF

	ans = INF

	for i in range(4):
		ans = min(ans, i + solve(clocks, switch + 1))
		push(clocks, switch)

	return ans

if __name__ == '__main__':
    C = int(input())
    for i in range(C):
	    clocks = list(map(int, input().split()))
	    ans = solve(clocks, 0)

	    if ans == INF:
		    print(INF)
	    else:
		    print(ans)



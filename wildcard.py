def wildcard(w, s): #패턴 w , 문자열 s w가 s에 대응되는지 여부 반환
    if (w, s) in cache:
        return cache[(w, s)]

    while s < len(S) and w < len(W) and (W[w] == '?' or W[w] == S[s]):
        w += 1
        s += 1
    # 패턴 끝에 도달해서 끝난경우 문자열도 끝
    if w == len(W):
        cache[(w, s)] = (s == len(S))
        return cache[(w, s)]

    if W[w] == '*':
        skip = 0
        while skip + s <= len(S):
            # * 만난경우 *에 몇글자를 대응할지 재귀를 통해 확인
            if wildcard(w + 1, s + skip):
                cache[(w, s)] = True
                return True
            skip += 1

    cache[(w, s)] = False
    # True 서로 대응 False 대응 X
    return False

C = int(input()) # 테스트 케이스 수
for i in range(C):
	W = input().strip() # 와카 문자열
	n = int(input()) # 파일명 수
	matches = []
	for j in range(n): #n줄에 하나씩 파일명이 주어짐
		S = input().strip()
		cache = {}
		if wildcard(0, 0):
			matches.append(S)

	matches.sort()
	for match in matches:
		print(match)
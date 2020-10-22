#1초뒤 이동가능 위치
# X-1
# X+1
# 2*X

from collections import deque

#수빈이는 N, 동생은 K
N, K = map(int, input().split())
Max = 10**5
arr = [-1]*(Max+1)
arr[N] = 0

queue = deque()
#수빈이 현재 위치
queue.append(N)

while(queue):
    x = queue.popleft()
    for nx in [x-1, x+1, 2*x]:
        if 0 <= nx <= Max and arr[nx] == -1:
            queue.append(nx)
            arr[nx] = arr[x] + 1

print(arr[K])
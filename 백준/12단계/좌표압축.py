# N 개의 좌표
N = int(input())
nums = list(map(int, input().split(' ')))
compressed = list(sorted(nums))

# 좌표 압축
# Xi를 좌표 압축한 결과는 Xi > Xj 를 만족하는 서로 다른 좌표의 개수와 같다

compressed = {compressed[i]: i for i in range(len(compressed))}
# print(compressed)

print(*[compressed[i] for i in nums])

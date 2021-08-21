# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만들기
# 단 배열의 인덱스에 해당하는 수가 연속해서 K번 초과하여 더해질 수 없음


# N개의 자연수, M번 더하기, 특정 인덱스에 해당하는 수가 K번 더해질 수 없음
N, M, K = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

nums.sort()

last_num = nums[-1]
last2_num = nums[-2]

ans = 0
while(M > 0):
    for i in range(K):
        ans += last_num  # 가장 큰수 k번 더해주기
        M -= 1
        if(M <= 0):
            break
    ans += last2_num
    M -= 1

print(ans)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(T):
    nums = list(map(int, input().split()))
    avg = sum(nums)/len(nums)
    print("#{} {}".format(i+1, round(avg)))
    
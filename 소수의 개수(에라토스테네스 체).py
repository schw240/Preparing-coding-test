n = int(input())
a=[0]*(n+1)
cnt = 0 #소수의 개수
for i in range(2,n+1):
    if a[i]==0:
        cnt+=1
    #밑에 반복문 처럼 작성하면 i만큼 증가하며 반복문 값 체크
    # 즉 맨 처음이 2부터 시작이므로 2씩 증가하여 2의 배수들 체크
    for j in range(i,n+1 , i):
        a[j]=1

print(cnt)
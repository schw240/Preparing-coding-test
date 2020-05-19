n = int(input())
a=list(map(int,input().split()))
score=0
bonus=0
for x in a:
    if x == 1:
        bonus+=1
        score+=bonus
    else:
        bonus=0

print(score)
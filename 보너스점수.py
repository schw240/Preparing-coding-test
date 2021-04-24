N, S = int(input()), input()

bonus = 0
score = 0
for i in range(N):
    if S[i] == 'O':
        score += (i+1) + bonus
        bonus += 1
    else:
        bonus = 0

print(score)

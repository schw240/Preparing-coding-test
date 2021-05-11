# H, M 현재 상근이가 설정해 놓은 알람 시간
# 창영이는 -45분으로 알람설정해둠

H, M = map(int, input().split(' '))

new_H, new_M = 0, 0

if M >= 45:
    new_H, new_M = H, M - 45
elif H > 0 and M < 45:
    new_H, new_M = H - 1, 60 + M - 45
else:
    new_H, new_M = 23, 60 + M - 45


print('{} {}'.format(new_H, new_M))

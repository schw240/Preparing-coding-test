words = input()
cnt = 0

for word in words:
    print(word, end="")
    cnt += 1
    if (cnt%10) == 0 :
        print("")
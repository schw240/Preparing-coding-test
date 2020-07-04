'''
input

4
FFFMMM
MMMFFF
FFFFF
FFFFFFFFFF
FFFFM
FFFFFMMMMF
MFMFMFFFMMMFMF
MMFFFFFMFFFMFFFFFFMFFFMFFFFMFMMFFFFFFF

output

1
6
2
2
''' 

def solve(member,fan):
    mm = int(member.replace("F", "0").replace("M", "1"),2)
    ff = int(fan.replace("F", "0").replace("M", "1"),2)

    print(member , fan)
    print(mm , ff)
    result = 0

    for i in range(len(fan) - len(member) + 1):
        if mm & ff == 0:
            result += 1
     
        ff = ff >> 1

    print("result:", result)

C = int(input())

if __name__ == '__main__':
    for i in range(C):
        mem = input()
        fan = input()
        solve(mem,fan)
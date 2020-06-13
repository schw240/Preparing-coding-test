'''
input

4
w
xbwwb
xbwxwbbwb
xxwwwbxwxwbbbwwxxxwwbbbwwwwbb

output

w
xwbbw
xxbwwbbbw
xxwbxwwxbbwwbwbxwbwwxwwwxbbwb

'''

def quadtree(test, index):
    ch = test[index]
    
    if ch == 'w':
        return ch
    if ch == 'b':
        return ch

    index += 1 #문자가 x인경우
    
    leftup = quadtree(test,index)
    index += len(leftup)

    rightup = quadtree(test, index)
    index += len(rightup)

    leftdown = quadtree(test,index)
    index += len(leftdown)

    rightdown = quadtree(test, index)

    return 'x' + leftdown + rightdown + leftup + rightup


if __name__ == '__main__':
    C = int(input())
    for i in range(C):
        test = input()
        print(quadtree(test, 0))

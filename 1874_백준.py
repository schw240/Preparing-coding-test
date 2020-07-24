'''
input

8
4
3
6
8
7
5
2
1

output

+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-
'''

result = []
stack = []
n = int(input())
count = 1

for i in range(n):
    a = int(input())
    while count <= a:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == a:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(result))

data_stack = list()


def push(data):
    data_stack.append(data)


def pop():
    data = data_stack[-1]
    del data_stack[-1]
    return data


for index in range(10):
    push(index)

print(pop())
print(data_stack)

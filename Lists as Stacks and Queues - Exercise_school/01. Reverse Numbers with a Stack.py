stack = input().split()
new_stack = []

for i in reversed(stack):
    new_stack.append(i)

print(" ".join(new_stack))
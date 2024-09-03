s = input()

stack = []

for simb in s:
    if len(stack) > 0 and stack[-1] == simb:
        stack.pop()
    else:
        stack.append(simb)

print(''.join(stack))
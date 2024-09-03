def h(c):
    return ord(c) - 97


table = [0] * 26

line = input()

for c in line:
    table[h(c)] += 1

print(max(table), end='')

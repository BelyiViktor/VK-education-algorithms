def h(c):
    return (ord(c) - 97) % 26


table_a = [0] * 26
table_b = [0] * 26

a, b = input().split(', ')

for c in a:
    table_a[h(c)] += 1
for c in b:
    table_b[h(c)] += 1

if table_a == table_b:
    print('true', end='')
else:
    print('false', end='')

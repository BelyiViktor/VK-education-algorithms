n = int(input())
sequence = list(map(int, input().split()))
k = int(input())
memo = 1
for i in range(k):
    memo *= sequence[i]
result = memo

left = 0
right = k
for i in range(0, n - k):
    memo /= sequence[left]
    memo *= sequence[right]
    result = max(result, memo)
    left += 1
    right += 1

print(int(result))

def last_even(arr):
    answer = []
    for elem in arr:
        if elem % 2 == 0:
            answer.append(elem)
    if len(answer) == 0:
        return -1
    else:
        return answer.pop()

_ = int(input())
print(last_even(list(map(int, input().split()))))

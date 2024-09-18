def change(arr):
    answer_front = []
    answer_end = []
    for val in arr:
        if val % 2 == 0:
            answer_front.append(val)
        else:
            answer_end.append(val)
    return answer_front + answer_end

n = int(input())
print(' '.join(map(str, change(list(map(int, input().split()))))))
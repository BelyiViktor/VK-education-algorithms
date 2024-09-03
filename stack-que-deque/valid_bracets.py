def isValid(bracket_sequence):
    stack = []
    brackets_dict = {'[': ']', '{': '}', '(': ')'}
    for bracket in bracket_sequence:
        if bracket in brackets_dict:
            stack.append(bracket)
        elif len(stack) == 0 or bracket != brackets_dict[stack.pop()]:
            return False
    return len(stack) == 0


print(isValid('{{{}}}]'))

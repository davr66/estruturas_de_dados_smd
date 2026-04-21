from collections import deque

def brackets_verifier(expression:str):
    stack = deque()
    opening_brackets = ['{','[','(']
    closing_brackets = ['}',']',')']
    for i,c in enumerate(expression):
        if c in opening_brackets:
            stack.appendleft((i,c))
        elif c in closing_brackets:
            if not stack:
                return i
            elif opening_brackets.index(stack[0][1]) != closing_brackets.index(c):
                return i
            else:
                stack.popleft()

    return -1 if not stack else stack[0][0]

print(brackets_verifier("(((q3jr)))"))
print(brackets_verifier("(a + [b * {c}])"))
print(brackets_verifier("([)]"))
print(brackets_verifier("((("))
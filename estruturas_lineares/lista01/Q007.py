from collections import deque

def palindrome_verifier(sentence:str):
    string = deque()
    for l in sentence.strip().lower():
        if l != " ": string.append(l)

    for _ in range(len(string)//2):
        left = string.popleft()
        right = string.pop()
        print(f"Comparando {left} = {right}")
        if  left != right:
            return False
    return True

print(palindrome_verifier("racecar"))
print(palindrome_verifier("A man a plan a canal Panama"))
print(palindrome_verifier("hello"))
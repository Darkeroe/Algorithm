import sys
input = sys.stdin.readline

ans,stack = '',[]
before = str(input())

for i in before:
    if i.isalpha():
        ans += i
    if i == '(':
        stack.append(i)
    elif i == '*' or i =='/':
        while stack and (stack[-1]=='*' or stack[-1]=='/'):
            ans+=stack.pop()
        stack.append(i)
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            ans+=stack.pop()
        stack.pop()

while stack:
    ans += stack.pop()
print(ans)

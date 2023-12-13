
before = '('
stack = []
contents = input()
result = 0

for content in contents:
    if content == "(":
        stack.append('(')
        before = '('
    elif content == ')':
        if before == '(':
            stack.pop()
            result += len(stack)
            before = ')'
        elif before == ')':
            stack.pop()
            result += 1
            before = ')'            
            
print(result)


#

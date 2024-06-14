n = int(input())

ans = [0] * n
A = list(map(int,input().split()))
stack = []

for i in range(n):
  while stack and A[stack[-1]] < A[i]:
    ans[stack.pop()] = A[i]
  stack.append(i)

while stack:
  ans[stack.pop()] = -1

result = ''
for i in range(n):
  result += str(ans[i]) + ' '
  
print(result)
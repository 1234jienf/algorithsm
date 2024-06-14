N = int(input())
A = list(map(int,input().split()))
S = [0] * N

## 삽입정렬

for i in range(1,N):
  insert_p = i
  insert_v = A[i]
  for j in range(i-1,-1,-1):
    if A[j] < A[i]:
      insert_p = j+1
      break
    if j == 0:
      insert_p = 0
  
  for j in range(i,insert_p,-1):
    A[j] = A[j-1]
  A[insert_p] = insert_v

S[0] = A[0]
for i in range(1,N):
  S[i] = S[i-1] + A[i]

sum = 0
for i in range(0,N):
  sum += S[i]
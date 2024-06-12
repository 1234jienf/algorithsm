## 시간초과


# N , M = map(int,input().split())

# arr = [list(map(int,input().split())) for _ in range(N)]

# for tc in range(M):
#   ans = 0
#   x1,y1,x2,y2 = map(int,input().split())
#   ## (x1,y1)부터 (y1,y2)까지
#   for i in range(x1,x2+1):
#     for j in range(y1,y2+1):
#       ans += arr[i-1][j-1]

#   print(ans)

# 구간합을 이용한 풀이

import sys
input = sys.stdin.readline

N, M = map(int,input().split())

A = [[0] * (N+1)]
D = [[0] * (N+1) for _ in range(N+1)]


for i in range(N):
  A_row = [0] + [int(x) for x in input().split()]
  A.append(A_row)

## 합 배열 만들기
for i in range(1,N+1):
  for j in range(1,N+1):
    D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for _ in range(M):
  x1,y1,x2,y2 = map(int,input().split())
  ans = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
  print(ans)
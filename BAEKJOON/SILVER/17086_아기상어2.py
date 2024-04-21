
## 문제

### N×M 크기의 공간에 아기 상어 여러 마리가 있다. 
### 간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 
### 한 칸에는 아기 상어가 최대 1마리 존재한다.

### 어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다. 
###  두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 이동은 인접한 8방향(대각선 포함)이 가능하다.
### 안전 거리가 가장 큰 칸을 구해보자. 

## 입력

### 첫째 줄에 공간의 크기 N과 M(2 ≤ N, M ≤ 50)이 주어진다.
### 둘째 줄부터 N개의 줄에 공간의 상태가 주어지며, 0은 빈 칸, 1은 아기 상어가 있는 칸이다.
### 빈 칸과 상어의 수가 각각 한 개 이상인 입력만 주어진다.

## 입력

### 첫째 줄에 안전 거리의 최댓값을 출력한다.


from collections import deque

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

v = [[0] * M for _ in range(N)]

dx = [0,0,1,1,1,-1,-1,-1]
dy = [1,-1,0,1,-1,1,-1,0]


def check(idx,i,j,f):
  if f != 0 :
    for k in range(8):
      nx = i + dx[k]
      ny = j + dy[k]
      if 0 <= nx < N and 0 <= ny < M:
        if arr[i][j] == 0 and v[i][j] == 0 or v[i][j] > idx:
          v[i][j] += 1
          check(idx,i,j)
        else:
          if v[i][j] <= idx:
            return
  else:
    for k in range(8):
      nx = i + dx[k]
      ny = j + dy[k]
      if 0 <= nx < N and 0 <= ny < M:
        if arr[i][j] == 0:
          v[i][j] += 1
          check(idx,i,j,f)
          return

      
a = 0
for i in range(N):
  for j in range(M):
    if arr[i][j] == 1:
      check(0,i,j,a)
      a += 1

ans = 0
for i in range(N):
  for j in range(M):
    ans = max(arr[i][j],ans)

print(v)
print(ans)

### BFS

## 너무 시간이 오래걸림 ㅜㅜ

# 연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 
# 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 
# 연구소는 빈 칸, 벽으로 이루어져 있다.


# 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

## 입력
# N,M (3 ≤ N, M ≤ 8)
# N개의 줄에 지도의 모양이 주어진다.
# 0은 빈 칸, 1은 벽, 2는 바이러스.
# 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
# 빈 칸의 개수는 3개 이상이다.

from collections import deque
import copy
import sys
input = sys.stdin.readline


# bfs 함수 : 
## 큐를 만든 후, 테스트 할 지도를 **깊은 복사** 함
## lab_map을 그대로 사용할 수 없다 -> 다시 0으로 되돌릴 수 없기 때문에
## 2가 위치한 곳을 큐에 넣어줌

dir = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs():
  q = deque()
  # q에 2의 위치를 전부 append 시켜줌
  tmp = copy.deepcopy(lab_map)
  for i in range(N):
    for j in range(M):
      if tmp[i][j] == 2:
        q.append((i,j))
  while q:
    r,c = q.popleft()

    for k in range(4):
      dr = r + dir[k][0]
      dc = c + dir[k][1]

      if (0 <= dr < N) and (0 <= dc < M):
        if tmp[dr][dc] == 0:
          tmp[dr][dc] = 2
          q.append((dr,dc))

  global result
  ans = 0
  for i in range(N):
    for j in range(M):
      if tmp[i][j] == 0:
        ans += 1
  result = max(result, ans)

# 지도 함수 : 
## 빈칸을 만날때 벽을 하나씩 세워주고 cnt를 1씩 증가시킨 후
## 총 세운 벽이 3개일때 bfs 함수 호출
## 주의: 밖으로 나왔을 시에 다시 빈칸으로 만들어줌
def wall(cnt):
  if cnt == 3:
    bfs()
    return
  for i in range(N):
    for j in range(M):
      if lab_map[i][j] == 0:
        lab_map[i][j] = 1
        wall(cnt+1)
        lab_map[i][j] = 0



N, M = map(int,input().split())
lab_map = [list(map(int,input().split())) for _ in range(N)]

result = 0
wall(0)

print(result)
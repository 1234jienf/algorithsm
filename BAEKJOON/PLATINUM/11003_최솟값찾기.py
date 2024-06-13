## 슬라이딩 윈도우 문제

import sys
from collections import deque

input = sys.stdin.readline


N, L = map(int,input().split())
q = deque()
now = list(map(int,input().split()))

for i in range(N):
  ## 제일 끝에 존재하는 숫자가 들어올 숫자보다 크면 pop한다.
  ## 최솟값을 찾는거니깐 큰 숫자는 필요가 없음
  while q and q[-1][0] > now[i]:
    q.pop()
  q.append((now[i],i))
  ## 윈도우 범위를 벗어나면
  if q[0][1] <= i - L:
    q.popleft()
  print(q[0][0], end=' ')
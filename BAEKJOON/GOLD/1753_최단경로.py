import sys
input = sys.stdin.readline

from queue import PriorityQueue

V,E = map(int,input().split())
K = int(input())
distance = [sys.maxsize] * (V+1)
visited = [0] * (V+1)
lst = [[] for _ in range(V+1)]
q = PriorityQueue()

## 인접 리스트 만들기
for _ in range(E):
  u,v,w = map(int,input().split())
  lst[u].append((v,w))

## 거리리스트에 출발 노드의 값을 0으로 설정
q.put((0,K))
distance[K] = 0

while q.qsize() > 0:
  current = q.get()
  c_v = current[1]
  if visited[c_v]:
    continue
  visited[c_v] = 1
  for tmp in lst[c_v]:
    next = tmp[0]
    value = tmp[1]
    if distance[next] > distance[c_v] + value:
      distance[next] = distance[c_v] + value
      q.put((distance[next], next))

for i in range(1,V+1):
  if visited[i]:
    print(distance[i])
  else:
    print('INF')
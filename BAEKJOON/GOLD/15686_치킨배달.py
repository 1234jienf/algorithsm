### DFS

## 크기가 N×N인 도시가 있다. 
## 도시는 1×1크기의 칸으로 나누어져 있다.
## 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다. 
## 도시의 칸은 (r, c)와 같은 형태로 나타내고,


## 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다
## 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

## 입력
# 첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)
# 둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.

# 도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다. 
# 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다
# 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

## 출력
# 첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때,
# 도시의 치킨 거리의 최솟값을 출력한다.

### 조합을 이용한 풀이

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int,input().split())

city_map = [list(map(int,input().split())) for _ in range(N)]
result = 999999
home = []
chicken =[]


for i in range(N):
  for j in range(N):
    if city_map[i][j] == 1:
      home.append([i,j])
    elif city_map[i][j] == 2:
      chicken.append([i,j])

## 폐업시키지 않을 치킨집 M개
for save_chicken in combinations(chicken,M):
    ans = 0
    for h in home:
        length  = 999
        for j in range(M):
            length = min(length, abs(h[0]-save_chicken[j][0]) + abs(h[1]-save_chicken[j][1]))
        ans += length
    result = min(result, ans)

print(result)

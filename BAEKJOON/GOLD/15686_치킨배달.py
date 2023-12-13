# DFS

N, M = map(int,input().split())

city_lst = [list(map(int,input().split())) for _ in range(N)]

home = []
chicken =[]
# 치킨집 좌표랑, 집 좌표 넣기
for i in range(N):
    for j in range(N):
        if city_lst[i][j] == 1:
            home.append((i,j))
        elif city_lst[i][j] == 2:
            chicken.append((i,j))
            




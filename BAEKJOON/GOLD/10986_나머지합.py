## 구간합 문제

N,M = map(int,input().split())
arr = list(map(int,input().split()))
d = []
d_lst = []
## 구간합 만들기
cnt = 0
answer = [0]* (M)
result = 0
## 1 3 6 7 9
for i in range(N):
  cnt += arr[i]
  d.append(cnt)


## 1 0 0 1 0
for num in d:
  d_lst.append(num % M)
for i in range(N):
  answer[d_lst[i]] += 1

for ans in answer:
  ## 개수 중 2개 고르는 경우의 수
  if ans >= 2:
    result += ans * (ans -1) // 2 

result += answer[0]

print(result)
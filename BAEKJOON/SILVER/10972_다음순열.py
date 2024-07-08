N = int(input())

## 순열
arr = list(map(int,input().split()))


def print_next_per(arr):
  i = len(arr) - 2
  while i >= 0 and arr[i] >= arr[i+1]:
    i -= 1

  if i == -1:
    return -1
  
  ## 해당해서 arr[i] 보다 arr[i+1]이 큰 수를 찾았다면 4 7 이런식으로 오름차순
  j = len(arr) - 1
  while arr[j] <= arr[i]:
    j -= 1
  
  arr[i], arr[j] = arr[j], arr[i]

  return(arr[:i + 1] + sorted(arr[i+1:]))

result = print_next_per(arr)

# 결과 출력
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))
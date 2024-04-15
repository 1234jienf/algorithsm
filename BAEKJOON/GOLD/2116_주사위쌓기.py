# 파이썬 답안

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

def max_num():
    result = []
    for i in range(6):
        sum = 0
        start = arr[0][i]
        for j in range(N):
            list1 = []
            index = arr[j].index(start)
            list1.append(start)
            if index == 0 or index == 5:
                start = arr[j][5-index]
                list1.append(start)
            elif index == 1 or index == 3:
                start = arr[j][4-index]
                list1.append(start)
            elif index == 2 or index == 4:
                start = arr[j][6-index]
                list1.append(start)
            complement = list(set(arr[j]) - set(list1))
            sum += max(complement)
        result.append(sum)
    result.sort()
    return result[-1]

print(max_num())


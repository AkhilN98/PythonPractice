n = int(input())
arr = map(int, input().split())
arr = sorted(arr)
arr_max = max(arr)
while max(arr)== arr_max:
    arr.remove(max(arr))
print(max(arr))5
n = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(n):
    if a[i] != i + 1:
        count = count + 1

if count == 2:
    print("YES")
else:
    print("NO")

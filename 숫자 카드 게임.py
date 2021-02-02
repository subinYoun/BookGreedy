n, m=map(int, input().split())
result=0
for i in range(n):
    a = list(map(int, input().split()))
    small = min(a)
    result = max(result, small)
print(result)
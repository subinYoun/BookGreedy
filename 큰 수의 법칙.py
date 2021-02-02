n, m, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
first_number = a[n-1]
second_number = a[n-2]
result = 0
while m >= k+1:
    result += (first_number*k)+second_number
    m -= k+1
result += m * first_number
print(result)
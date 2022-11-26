n, k = map(int, input().split())
k = len(k)

res = 1

if n % k != 0:
    b = n % k
else:
    b = k

for i in range(n, b, -k):
    res *= i

print(res)
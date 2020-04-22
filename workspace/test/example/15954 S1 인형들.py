n, k = map(int, input().split())
like = list(map(int, input().split()))
ans = 2100000000

for j in range(k, n):
    for i in range(n-j+1):
        var = [(x-sum(like[i:i+j]) / len(like[i:i+j]))**2 for x in like[i:i+j]]
        std = (sum(var) / len(var))**(1/2)
        ans = min(ans, std)
print(ans)
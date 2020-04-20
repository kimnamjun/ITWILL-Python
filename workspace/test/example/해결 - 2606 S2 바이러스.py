def find(x):
    return x if x == boss[x] else find(boss[x])


def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        boss[y] = x
    elif x > y:
        boss[x] = y


n = int(input())
boss = dict()
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a not in boss:
        boss[a] = a
    if b not in boss:
        boss[b] = b
    union(a, b)

ans = 0
for i in boss:
    if find(i) == 1:
        ans += 1
print(ans - 1)
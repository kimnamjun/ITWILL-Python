for _ in range(int(input())):
    ans = 0
    x1, y1, x2, y2 = map(int, input().split())
    for _ in range(int(input())):
        cx, cy, r = map(int, input().split())
        a = 1 if (cx - x1) * (cx - x1) + (cy - y1) * (cy - y1) < r * r else 0
        b = 1 if (cx - x2) * (cx - x2) + (cy - y2) * (cy - y2) < r * r else 0
        if a - b:
            ans += 1
    print(ans)
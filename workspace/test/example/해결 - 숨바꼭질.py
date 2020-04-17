n, k = map(int, input().split())
time = 0

odd = set()
even = {n}
odd_new = set()
even_new = {n}

while True:
    now, nxt, old, new \
        = (odd, even, odd_new, even_new) if time % 2 else (even, odd, even_new, odd_new)

    if k in now:
        break

    for i in old:
        if i + 1 not in nxt and i < 100000:
            nxt.add(i + 1)
            new.add(i + 1)
        if i - 1 not in nxt and i > 0:
            nxt.add(i - 1)
            new.add(i - 1)
        if i * 2 not in nxt and i < 70000:
            nxt.add(i * 2)
            new.add(i * 2)
    old.clear()

    time += 1

print(time)

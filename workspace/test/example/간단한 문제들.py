# 2193 S3 이친수

n = int(input())

if n == 1 or n == 2:
    print(1)
elif n == 3:
    print(2)
else:
    s = 3
    tab = list()
    tab.append([1])
    tab.append([1])
    while 1:
        tab[0].append(tab[0][-1] + tab[1][-1])
        tab[1].append(tab[0][-2])

        if s == n:
            print(tab[0][-1] + tab[1][-1])

        s += 1

# 1 1 2 5
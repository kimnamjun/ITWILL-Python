def find(x):
    if x == index[x]:
        return x
    new = find(index[x])
    x = new
    return new


def union(x1, y1):
    x, y = find(x1), find(y1)
    if x != y:
        if length[x] < length[y]:
            index[y] = x
        else:
            index[x] = y


index = dict()
length = dict()

line = input()
token = line.split('&&')
print(token)
for i in token:
    if i.find('==') != -1:
        j = i.split('==')
        if j[0] not in index:
            index[j[0]] = j[0]
            length[j[0]] = len(j[0])
        if j[1] not in index:
            index[j[1]] = j[1]
            length[j[1]] = len(j[1])
        union(j[0], j[1])

print(index)
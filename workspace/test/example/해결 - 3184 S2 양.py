import sys

sys.setrecursionlimit(1000000)

def dfs(y, x, color):
    if visit[y][x] != 0 or board[y][x] == '#':
        return
    visit[y][x] = color
    if y > 0:
        dfs(y-1, x, color)
    if x > 0:
        dfs(y, x-1, color)
    if x < col-1:
        dfs(y, x+1, color)
    if y < row-1:
        dfs(y+1, x, color)

row, col = map(int, sys.stdin.readline().strip().split())

board = list()
visit = list()
for _ in range(row):
    data = sys.stdin.readline().strip()
    board.append(data)
    visit.append([0]*col)

color = 0
o = dict()
v = dict()
for idx1, val1 in enumerate(board):
    for idx2, val2 in enumerate(val1):
        if visit[idx1][idx2] == 0 and board[idx1][idx2] != '#':
            color += 1
            dfs(idx1, idx2, color)

for idx1, val1 in enumerate(board):
    for idx2, val2 in enumerate(val1):
        if board[idx1][idx2] == 'o':
            o[visit[idx1][idx2]] = o.get(visit[idx1][idx2], 0) + 1
        elif board[idx1][idx2] == 'v':
            v[visit[idx1][idx2]] = v.get(visit[idx1][idx2], 0) + 1

num_o = 0
num_v = 0
for i in o:
    if o[i] > v.get(i, 0):
        num_o += o[i]
for i in v:
    if v[i] >= o.get(i, 0):
        num_v += v[i]
print(num_o, num_v)

import sys
sys.setrecursionlimit(1000000)


def dfs(y, x, clr):
    stk = [(y,x)]
    while stk:
        a, b = stk.pop()
        visit[a][b] = clr
        if y > 0 and visit[idx1][idx2] == 0 and board[idx1][idx2] != '#':
            stk.append((y-1, x))
        if x > 0:
            stk.append((y, x-1))
        if x < col - 1:
            stk.append((y, x+1))
        if y < row - 1:
            stk.append((y+1, x))

row, col = map(int, sys.stdin.readline().split())

board = list()
visit = list()
for _ in range(row):
    data = sys.stdin.readline()[:-1]
    board.append(data)
    visit.append([0]*col)

color = 0
for idx1, val1 in enumerate(board):
    for idx2, val2 in enumerate(val1):
        if visit[idx1][idx2] == 0 and board[idx1][idx2] != '#':
            color += 1
            dfs(idx1, idx2, color)

o = dict()
v = dict()
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
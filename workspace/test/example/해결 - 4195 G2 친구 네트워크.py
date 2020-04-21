# https://chancoding.tistory.com/50

def F(X):
    if X == P[X]:
        return X
    W = F(P[X])
    P[X] = W
    return W

def U(X, Y):
    X, Y = F(A), F(B)
    if X != Y:
        P[Y] = X
        N[X] += N[Y]
    print(N[X])

for _ in range(int(input())):
    N, P = {}, {}
    for _ in range(int(input())):
        A, B = input().split()
        if A not in P:
            P[A] = A
            N[A] = 1
        if B not in P:
            P[B] = B
            N[B] = 1
        U(A, B)
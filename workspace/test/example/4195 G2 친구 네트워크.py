for _ in range(int(input())):
    N={}
    for _ in range(int(input())):
        A,B=input().split()
        if A in N:
            if B in N:
                if id(N[A])!=id(N[B]):
                    N[A][0]+=N[B][0]
                    N[B]=N[A]
            else:
                N[A][0]+=1
                N[B]=N[A]
        else:
            if B in N:
                N[B][0]+=1
                N[A]=N[B]
            else:
                N[A]=[2]
                N[B]=N[A]
        print(N[A][0])

# 에러 케이스
'''
1
4
a b 2
c d 2
a c 4
b d 6
'''
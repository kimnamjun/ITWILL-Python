class A:
    def __init__(self, a):
        self.a = a

    class C:
        def __init__(self, c):
            self.c = c

class B:
    def __init__(self, b):
        self.b = b

class D(A, B):
    def __init__(self, a, b, d):
        A.__init__(self, a)
        B.__init__(self, b)
        self.d = d

d1 = D(1, 2, 3)
print(d1.a)
print(d1.b)
print(d1.d)
class X:
    pass
class A(X):
    pass
class B(X):
    pass
class C(X):
    pass
class P(A, B):
    pass
class Q(A, C):
    pass
class Y(P, Q):
    pass
class Z(Y):
    pass

print(Z.mro())
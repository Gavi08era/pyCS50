def f(n):
    if n<=1:
        return n
    last=f(n-1)
    prelast=f(n-2)
    return last+ prelast
n=4
print(f(n))
def dojob(n):
    if n<=5:
        return
    dojob(n-1)
    print(n)
    dojob(n-1)
    print(n)
dojob(8)
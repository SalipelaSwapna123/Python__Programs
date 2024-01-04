def f(n):
    if n<=0:
        return -1
    if n==1:
        return 0
    if n==2:
        return 1
    a,b=0,1
    res=a+b
    for i in range(0,n-2):
       next=a+b
       res=res+next
       a=b
       b=next
    print(res)

f(10)
def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return -1 
    return 1
def primesmall(n):
    while n>0:
        if prime(n) == 1:
            return n
        else:
            n=n-1
def primelarge(n):
    while True:
        if prime(n) == 1:
            return n
        else:
            n=n+1
t = int(input())
while t>0:
    max1 = 0
    min2 = 0
    ls=[]
    c=1
    res=0
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n-1):
        max1 = primelarge(a[i])
        min2 = primesmall(a[i+1])
        if min2 >= max1:
            c=c+1
        else:
            ls.append(c)
            c=1
    ls.append(c)
    res = max(ls)
    print(res)
    t-=1

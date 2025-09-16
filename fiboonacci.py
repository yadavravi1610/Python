n= int(input())

def myfun(n):
    if n==1 or n==2:
        return 1
    return myfun(n-1) + myfun(n-2)

ans = myfun(n)

print(ans)
n = int(input())

def myfun(n):
    if n==0:
        return 1
    return n * myfun(n-1)

ans = myfun(n)

print(ans)
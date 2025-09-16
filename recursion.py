
# this will create an stack overflow
# n= int(input())

# def fun(n):
#     print(n)
#     fun(n-1)

# fun(3)

# to resolve this we have to give the base condition

n= int(input())

def fun(n):
    if n==1: # base condition
        return 1
    return n + fun(n-1)
    # fun(n-1)

ans = fun(n)    

print(ans)
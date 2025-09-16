# a = int(input())
# b = int(input())

# def sum(a,b):
#     print(a+b)

# sum(a,b)    

# If we give more arguments than parameters it will show error instead of that in parameters we can take *num

a = int(input())
b = int(input())

def sum(*numbers):
    s = 0
    for n in numbers:
        s+=n
    print(s)

sum(a,b,8)   
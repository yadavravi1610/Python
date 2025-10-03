# def stringJumper(s):
#     for i in range(0,len(s),2):

#         print(s[i], end="")


# stringJumper(input())

# def printInDecreasing(x):
#     while (x >= 0):
#         print(x,end=" ")
#         x -= 1

# printInDecreasing(int(input()))       
# 

# def printIncreasingPower(x):
#     n =1
#     while( n<=x):
#         if(n*n <= x):
#             print (n*n , end = " ")
        
#         n += 1 
# printIncreasingPower(int(input()))

def pos(n):
    x=0
    while (n>x):
        n -= 1
        print(n, end=" ")
        
    
def neg(n):
    x=0
    while (n<=x):
        print(n, end=" ")
        n += 1

n = int(input())

if(n> 0):
    pos(n)
elif(n<0):
    neg(n)
elif(n == 0):
    print("Already Zero")        
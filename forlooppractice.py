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

def printIncreasingPower(x):
    n =1
    while( n<=x):
        if(n*n <= x):
            print (n*n , end = " ")
        
        n += 1 
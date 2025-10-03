# def stringJumper(s):
#     for i in range(0,len(s),2):

#         print(s[i], end="")


# stringJumper(input())

def printInDecreasing(x):
    while (x >= 0):
        print(x,end=" ")
        x -= 1

printInDecreasing(int(input()))        
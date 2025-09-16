
# n=3

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if j<=i:
#             print("#", end="") 
#         else:
#             print("", end="")
#     print("")   

# n=3

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if j >= n+1- i:
#             print("*", end="") 
#         else:
#             print(" ", end="")
#     print("") 

n=4
k=1
for i in range(1, n+1):
    for j in range(1, n+1):
        if j <= i:
            print(k, end="")
            k+=1 
        else:
            print(" ", end="")
    print("") 
# m=3
# n=3
# list = []
# for i in range(m):
#     for j in range(n):
#         list.extend(int(input().split()))

# print(list)

m = int(input())
# n = int(input())

# list = []
# for i in range(m):
#     tempList = [int(ele) for ele in input().split()] #shorthand of taking input for list in list
#     list.append(tempList)
# print(list)

list = []
for i in range(m):
 #shorthand of taking input for list in list
    list.append([int(ele) for ele in input().split()])

for i in range(m):
    for j in range(m):
        if j<=i:
            print(list[i][j], end=" ")
    print()

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

# for i in range(m):
#     for j in range(m):
#         if j<=i:
#             print(list[i][j], end=" ")
#     print() #After finishing a row, this prints an empty line → moves to the next row.

# trace = [list[i][j] for i in range(m) for j in range(m) if j<=i]
# print(trace)

for i in range(m):
    for j in range(m):
        if j > i:
            temp = list[j][i]
            list[j][i] = list[i][j]
            list[i][j] = temp

print(list)            
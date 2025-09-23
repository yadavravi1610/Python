# m=3
# n=3
# list = []
# for i in range(m):
#     for j in range(n):
#         list.extend(int(input().split()))

# print(list)

m = int(input())
n = int(input())

list = []
for i in range(m):
    tempList = [int(ele) for ele in input().split()] #shorthand of taking input for list in list
    list.append(tempList)
print(list)
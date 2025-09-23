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
    tempList = input().split()
    for j in range(n):
        tempList[j] = int(tempList[j])
    list.append(tempList)    

print(list)
lists = input().split()

for i in range(len(lists)):
    lists[i] = int(lists[i])

# sum = 0
# for i in range(len(lists)):
#     sum += lists[i]

print(sum(lists))
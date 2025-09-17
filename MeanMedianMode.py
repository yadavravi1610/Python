lists = input().split()

for i in range(len(lists)):
    lists[i] = int(lists[i])

sum = 0

for i in lists:
    sum += i

mean = sum // len(lists)
print(mean)


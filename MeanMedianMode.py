lists = input().split()

for i in range(len(lists)):
    lists[i] = int(lists[i])

sum = 0

for i in lists:
    sum += i

mean = sum // len(lists)
print(mean)

if len(lists)%2 != 0:
    median = len(lists)//2
    print("Median for odd numbers = ", lists[median])
if len(lists)%2 == 0:
    median1 = len(lists)//2
    # median2 = len(lists)+1//2
    print("Median for even numbers =", lists[median1], ",", lists[median1+1])
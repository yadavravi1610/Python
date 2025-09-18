n = int(input())

lists = input().split()

for i in range(n):
    lists[i] = int(lists[i])

sum = 0

for i in lists:
    sum += i

mean = sum // n
print(mean)

lists.sort()

print(lists)
if n%2 != 0:
    median = n//2
    print("Median for odd numbers = ", lists[median])
if n%2 == 0:
    median1 = n//2
    print(median1)
    median2 = n//2 - 1
    print(median2)
    median = (lists[median1] + lists[median2] )// 2
    print(median)
    print("Median for even numbers =", median)
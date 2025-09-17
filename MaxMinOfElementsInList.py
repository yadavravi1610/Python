
lists = input().split()

for i in range(len(lists)):
    lists[i] = int(lists[i])

max = lists[0]
min = lists[0]

for i in range(len(lists)):              # for i in lists:
    if min > lists[i]:                   #     if min > i               
        min = lists[i]                   #         min = i
    if max < lists[i]:                   #     if max <i
        max = lists[i]                   #         max = i

print(max, min)
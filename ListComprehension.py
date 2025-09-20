# list =  [ele for ele in range(5)]

#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list

#We can perform operation on first ele to alter the list like ele*2 that means it will multiple 2 with each
#element in list

# print(list)

list = [int(ele) for ele in input().split()] # Using this we can take input in list and default it is string
#So for that we will typecase our element
# print(list) 

list1 = [ele*ele for ele in list]
print(list1)

# we can create new list by using values of existing list
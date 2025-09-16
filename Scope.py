var = 2

def function():
    var = 5  #local scope
    print(var)

function()
print(var) #global scope

# var = 2

# def function():
#     global var # to use the global variable inside a local scope we have to user global keyword
#     var +=1
#     print(var)

# function()
# print(var)

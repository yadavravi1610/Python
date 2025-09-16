var = 2

def function():
    global var # to use the global variable inside a local scope we have to user global keyword
    var +=1
    print(var)

function()
print(var)

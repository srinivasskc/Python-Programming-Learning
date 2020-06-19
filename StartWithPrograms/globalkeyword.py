#global variable will be created inside a function.
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is "+x)

y="awesome"
def myfunc():
    global y
    y = "fantastic"
myfunc()
print("python is " + y)

"""
global z = "awesome"
# we cannot declare global outside the function.
def myfunc():
    z="fantastic"
myfunc()
print("Python is " + z)
"""

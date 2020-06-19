#global variable

x=300
def myfunc():   #if we dont give colon for the def of func, it will throw syntax error.
    print(x)
myfunc()
print(x)
print()

#global and local variables
x=300
def myfunc():
    x=200
    print(x)
myfunc()
print(x)


# global keyword
print("Global Keyword")

def myfunc():
    global x
    x = 300
    print("Inside function: ", x)
myfunc()
print("Outside function: ", x)
print()

#global variable - global keyword
print("global variable - global keyword")

x=300
def myfunc():
    #global x = 200  we cannot initialize and assign at the same time.
    global x
    x=200
    print("Inside function: " , x)
myfunc()
print("outside function: " , x) #This will overwrite the value which is declared as 200 to 300




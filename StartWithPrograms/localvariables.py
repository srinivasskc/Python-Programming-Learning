#local variables

def myfunc():
    x=300
    print(x)
myfunc()


#function inside function

def myfunc():
    x=300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

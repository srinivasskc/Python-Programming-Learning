#local variables from one function are completely separate from another function.

def spam():
    eggs=20
    bacon()
    print("Local Spam - eggs Scope: "+str(int(eggs)))

def bacon():
    ham=30
    eggs=0
    print("Local bacon - ham Scope: "+str(int(ham)))
    print("Local bacon - eggs Scope: "+str(int(eggs)))
    

spam()

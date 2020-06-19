spam = 42 #global variable - scope

def eggs():
    global spam  #global keyword is called: It will overwrite gloval variable value with local variable.
    spam = 30 #local variable - scope ==> As glo
    print("Local Variable Spam: " + str(int(spam)))

eggs()
print("Global Variable Spam: "+ str(int(spam)))

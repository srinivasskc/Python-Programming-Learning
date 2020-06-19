spam = 42 #global variable - scope

def eggs():
    spam = 30 #local variable - scope
    print("Local Variable Spam: " + str(int(spam)))

eggs()
print("Global Variable Spam: "+ str(int(spam)))

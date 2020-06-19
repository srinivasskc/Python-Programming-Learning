passwordFile = open("E://Python//Programs//ATBS With Python//Day 1 - 20 Feb//SecretPasswordFile.txt")
secretPassword = passwordFile.read()
print('Enter your password')
typedPassword = input()
if typedPassword == secretPassword:
    print("access granted")
    ##if typedPassword == '12345':
       ## print("No one will enter weak password")
else:
        print("access denied")
    

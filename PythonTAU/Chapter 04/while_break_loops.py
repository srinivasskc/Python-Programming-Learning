temp_c = 40
print("Temperature is {}, It is Hot Summer".format(temp_c))

while temp_c >27:
    print("Temperature is {} and weather is sunny ".format(temp_c))
    #temp_c = temp_c-1
    temp_c -= 1
    if temp_c == 28:
        break
#print("Temperature is less than {}, It is Winter".format(temp_c))



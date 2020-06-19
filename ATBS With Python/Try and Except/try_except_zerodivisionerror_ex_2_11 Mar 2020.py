def div42bynumber(divideby):
    try:
        return 42/divideby
    except:  #without mentioning error detail.
        print("Error. You tried division by Zero")

print(div42bynumber(2))
print(div42bynumber(1))
print(div42bynumber(0))   #Returns Error Statement and Return Value - None
print(div42bynumber(12))




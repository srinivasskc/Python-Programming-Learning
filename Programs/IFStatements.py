# If Statements in Python

# If Else

is_male = False

if is_male:
    print("Yes, You are a Male")
else:
    print("You are not a Male")

# If Else

is_male = True
is_tall = True

if is_male or is_tall:
    print("You are Male or You are Tall")
else:
    print("You are neither Male nor Tall")


# If Elif Else
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are Tall Male")
elif is_male and not is_tall:
    print("You are Short Male")
elif not is_male and is_tall:
    print("You are not male, But you are Tall")
else:
    print("You are neither Male nor Tall")


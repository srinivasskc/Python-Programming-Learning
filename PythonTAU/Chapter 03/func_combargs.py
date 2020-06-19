def application(name, age, email, company, *args, **kwargs):
    """
    name, age, email, company are formal positional arguments,
    *args, **kwargs - unlimited arguments and variables
    """

    print("{} is of age {} and email is {}, working for {}".format(name,age,email,company))

    print(args)
    print(kwargs)

application("Srinivas", 25, "sk@mail.com", "Moolya",75000, 45000, 12000, hire_date="20-9-2018", confirm_date="30-12-2018")
#args, *args, **kwargs

# application("Srinivas", 25, "sk@mail.com", "Moolya",75000, "20-9-2018")

#print(*args)
#print(**kwargs)
#Error is returned for the below func call
#application("Srinivas", 25, "sk@mail.com", "Moolya",75000, hire_date="20-9-2018")
#args, *args, **kwargs

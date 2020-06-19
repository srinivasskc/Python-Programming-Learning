"""
Keyword Arguments:
  We can set some default values to the arguments
"""

def user_info(name, age=0, city="New York"):
    """
    :param name:
    :param age:
    :param city:
    :return:
    """
    print("{} is of age {}, and is from {} city".format(name,age,city))


user_info("Srinivas", 30, "Bangalore")
user_info("Kadiyala")

#With Keyword Arguments, we can call the arguments in any order
user_info(age=25, name="Srini",city="Hyderabad")

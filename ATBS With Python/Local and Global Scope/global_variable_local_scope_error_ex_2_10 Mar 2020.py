def eggs(): #no local variable
    print("eggs: "+str(int(eggs)))

eggs=20 #global variable
eggs()

"""
Traceback (most recent call last):
  File "E:/Python/Programs/ATBS With Python/Day 7 - 10 Mar/global_variable_local_scope_error_ex_2_10 Mar 2020.py", line 5, in <module>
    eggs()
TypeError: 'int' object is not callable
>>>

"TypeError 'int' or 'float' object is not callable"
It probably means that you are trying to call a method
when a property with the same name is available.
If this is indeed the problem, the solution is easy.
Simply change the method call into a property access.
"""

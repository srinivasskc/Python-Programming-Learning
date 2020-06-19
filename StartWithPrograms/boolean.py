#boolean expression comparison

print(10<9)
print(10 == 9)
print(10 > 9)


#if statement
a=223
b=5

if b > a:    #false
    print("b is greater than a")
else:
    print("b is not greater than a")  #prints else statement.


#Evaluate values using Bool Function - By default, it is true if it has some content.
print(bool("Hello"))
print(bool(15))

#any string is true, except for empty string
print(bool())

#any value is true, except for zero
print(bool(0))

print("===Evaluating two variables===")

#Evaluating two variables

x="Hello"
y=15
print(bool(x))  #true
print(bool(y))  #true

print("===List, Tuple, Set and Dictionary === ")


#Evaluating the list, tuple, set and dictionary

list = [123,142,165,"Hello"]
tuple = ["Jan","Feb","Mar"]
dictionary = {"Peter" : 38, "John" : 25}
dict = dict(peter=38,john=25)

print(bool(list))  #true
print(bool(tuple)) #true
print(bool(dictionary)) #true
print(bool(dict)) #true



#functions that can return a boolean value
# built-in function: isinstance() - can determine if object is of certain data type.
print("====isinstance() function === ")

x=2300
print(isinstance(x,int)) #true
print(isinstance(x,float))  #false






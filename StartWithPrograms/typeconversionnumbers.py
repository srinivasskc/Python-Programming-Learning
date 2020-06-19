
#type conversion

a=1
b=2.8
c=3+5j   #Complex numbers are written with a "j" as the imaginary part:


print(a)
x=float(a) 
print(x)
print()

print(b)
y=int(b)  #decimal is ignored and 2 will be displayed.
print(y)
print()

print(c)
z=complex(x)  #1+0j
print(z)

i=complex(b) #2.8+0j
print(i)

z=1j
print(z)


"""
l=int(z) #cannot convert complex to int.
print(l)
"""

"""
m=float(z) #cannot convert complex to foat
print(m)
"""

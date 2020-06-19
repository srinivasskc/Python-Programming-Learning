list function with range:

>>> list(range(2))
[0, 1]


for loop with range:
>>> for i in range(2):
	print(i)

0
1

for loop with range:
>>> for i in range(0,2):
	print(i)

0
1

for loop with list values:
>>> for i in [0,1]:
	print(i)

0
1

range object - range(start, stop):
>>> range(0,100)
range(0, 100)

range object - range(start, stop, step)
>>> range(0,100,2)
range(0, 100, 2)
>>> list(range(0,100,2))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> 

Assigning to a variable:
>>> spam = list(range(0,50,2))
>>> spam
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]



For Loop:
>>> supplies = ['pens', ' staplers' , 'flames', 'binders']
>>> range(len(supplies))
range(0, 4)

for i in range(len(supplies)):
	print("Index " + str(i) + "in Supplies is: "+ supplies[i])

Index 0in Supplies is: pens
Index 1in Supplies is:  staplers
Index 2in Supplies is: flames
Index 3in Supplies is: binders
>>> 
>>> supplies[1]
' staplers'




Multiple Assignments.

>>> cat = ["fat", "black", "loud"]
>>> size = cat[0]
>>> size
'fat'
>>> color = cat[1]
>>> color
'black'
>>> disposition = cat[2]
>>> disposition
'loud'
>>> cat
['fat', 'black', 'loud']
>>> 
>>> sizes, colors, dispositions = cat
>>> sizes
'fat'
>>> colors
'black'
>>> dispositions
'loud'
>>> 



>>> size, color, disposition = 'zero size', 'white', 'calm'
>>> size
'zero size'
>>> color
'white'
>>> disposition
'calm'


Swapping Variables:
>>> 
>>> a = "abc"
>>> b = "cab"
>>> a
'abc'
>>> b
'cab'
>>> a,b = b,a
>>> a
'cab'
>>> b
'abc'
>>> 



Increment
>>> 
>>> spam = 42
>>> spam
42
>>> spam = spam + 1
>>> spam
43
>>> 

Augmented Assignment
>>> spam += 1
>>> spam
44
>>> spam -= 1
>>> spam
43
>>> spam *= 1
>>> spam
43
>>> spam /= 1
>>> spam
43.0
>>> 

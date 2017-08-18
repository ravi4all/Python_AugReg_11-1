Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> fred = turtle.Pen()
>>> fred.forward(100)
>>> fred.left(45)
>>> fred.left(45)
>>> fred.left(45)
>>> fred.reset()
>>> fred.forward(100)
>>> fred.left(135)
>>> fred.forward(100)
>>> fred.left(135)
>>> fred.left(135)
>>> fred.left(135)
>>> fred.left(45)
>>> fred.forward(100)
>>> fred.reset()
>>> fred.forward(100)
>>> fred.left(135)
>>> fred.forward(200)
>>> fred.reset()
>>> fred.forward(200)
>>> fred.left(135)
>>> fred.forward(150)
>>> fred.left(90)
>>> fred.forward(150)
>>> for i in range(5):
	col = random.choice(colors)
	fred.color(col)
	fred.forward(200)
	fred.left(135)
	fred.forward(150)
	fred.left(90)
	fred.forward(160)

	
Traceback (most recent call last):
  File "<pyshell#26>", line 2, in <module>
    col = random.choice(colors)
NameError: name 'random' is not defined
>>> import random
>>> fred.reset()
>>> for i in range(5):
	col = random.choice(colors)
	fred.color(col)
	fred.forward(200)
	fred.left(135)
	fred.forward(150)
	fred.left(90)
	fred.forward(160)

	
Traceback (most recent call last):
  File "<pyshell#30>", line 2, in <module>
    col = random.choice(colors)
NameError: name 'colors' is not defined
>>> colors = ['red','green','blue','orange']
>>> for i in range(5):
	col = random.choice(colors)
	fred.color(col)
	fred.forward(200)
	fred.left(135)
	fred.forward(150)
	fred.left(90)
	fred.forward(160)

	
>>> fred.reset()
>>> for i in range(5):
	col = random.choice(colors)
	fred.color(col)
	fred.forward(200)
	fred.left(135)
	fred.forward(150)
	fred.left(90)
	fred.forward(210)

	
>>> fred.reset()
>>> for i in range(5):
	col = random.choice(colors)
	fred.color(col)
	fred.forward(200)
	fred.left(135)
	fred.forward(150)
	fred.left(90)
	fred.forward(160)
	fred.left(90)

	
>>> fred.reset()
>>> fred.speed(1)
>>> for i in range(5):
	col = random.choice(colors)
	fred.color(col)
	fred.forward(200)
	fred.left(135)
	fred.forward(150)
	fred.left(90)
	fred.forward(160)
	fred.left(90)

	
>>> fred.reset()
>>> for i in range(5):
	col = random.choice(colors)
	fred.color(col)
	fred.forward(200)
	fred.left(135)
	fred.forward(150)
	fred.left(90)
	fred.forward(160)
	fred.left(135)

	
>>> fred.reset()
>>> for i in range(5):
	col = random.choice(colors)
	fred.color(col)
	fred.forward(i+10)
	fred.left(135)
	fred.forward(i+5)
	fred.left(90)
	fred.forward(i+6)
	fred.left(135)

	
>>> fred.reset()
>>> for i in range(5):
	col = random.choice(colors)
	fred.color(col)
	fred.forward(i+100)
	fred.left(135)
	fred.forward(i+50)
	fred.left(90)
	fred.forward(i+60)
	fred.left(135)

	
>>> fred.reset()
>>> for i in range(5):
	col = random.choice(colors)
	fred.color(col)
	fred.forward(i+100)
	fred.left(135)
	fred.forward(i+50)
	fred.left(90)
	fred.forward(i+60)
	fred.left(135)

	
>>> a = 10
>>> id(a)
1440634752
>>> id(10)
1440634752
>>> b = a
>>> id(b)
1440634752
>>> a = ["Hello","Python","Programming"]
>>> a[0]
'Hello'
>>> a[1]
'Python'
>>> b = a
>>> b
['Hello', 'Python', 'Programming']
>>> b[0] = "Bye"
>>> b
['Bye', 'Python', 'Programming']
>>> a
['Bye', 'Python', 'Programming']
>>> a = ["Hello","Python","Programming"]
>>> b = a.copy()
>>> b
['Hello', 'Python', 'Programming']
>>> a
['Hello', 'Python', 'Programming']
>>> b[0] = "Bye"
>>> b
['Bye', 'Python', 'Programming']
>>> a
['Hello', 'Python', 'Programming']
>>> a = 10.839478934573489758934758934
>>> type(a)
<class 'float'>
>>> a = True
>>> a
True
>>> if a
SyntaxError: invalid syntax
>>> a = 10
>>> b = "10"
>>> a == b
False
>>> a is b
False
>>> b = 10
>>> a is b
True
>>> a = "10"
>>> b = "10"
>>> a is b
True
>>> a = ["Hello","Python","Programming"]
>>> "Hello" in a
True
>>> "Hello" not in a
False
>>> a is not b
True
>>> def func():
	return 1,2,3,4,5

>>> func()
(1, 2, 3, 4, 5)
>>> a,b,c,d,e = func()
>>> a
1
>>> b
2
>>> c
3
d
>>> 
>>> e
5
>>> a = "Hello Python Programming"
>>> a.split()
['Hello', 'Python', 'Programming']
>>> len(a)
24
>>> a.count)(
	
SyntaxError: invalid syntax
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    a.count()
TypeError: count() takes at least 1 argument (0 given)
>>> b = a.split()
>>> b
['Hello', 'Python', 'Programming']
>>> len(b)
3
>>> len(a.split())
3
>>> a
'Hello Python Programming'
>>> size = height, width = 100, 200
>>> size
(100, 200)
>>> height
100
>>> width
200
>>> a,b = 10, 12
>>> a,b = b,a
>>> a
12
>>> b
10
>>> a,b = 10, 12
>>> a
10
>>> b
12
>>> b,a = a,b
>>> b
10
>>> a
12
>>> 

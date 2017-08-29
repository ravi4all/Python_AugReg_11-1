Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [1,2,3,4,5]
>>> b = ['a','e','i','o','u']
>>> for i in a,b:
	print(i)

	
[1, 2, 3, 4, 5]
['a', 'e', 'i', 'o', 'u']
>>> for i,j in a,b:
	print(i)
	print(j)

	
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    for i,j in a,b:
ValueError: too many values to unpack (expected 2)
>>> z = zip(a,b)
>>> z
<zip object at 0x0000016F29F36B08>
>>> z = list(zip(a,b))
>>> z
[(1, 'a'), (2, 'e'), (3, 'i'), (4, 'o'), (5, 'u')]
>>> for i in z:
	print(i)

	
(1, 'a')
(2, 'e')
(3, 'i')
(4, 'o')
(5, 'u')
>>> for i in range(0,5):
	for j in range(1,i+1):
		print("*")

		
*
*
*
*
*
*
*
*
*
*
>>> for i in range(0,5):
	for j in range(1,i+1):
		print("*")
	print()

	

*

*
*

*
*
*

*
*
*
*

>>> for i in range(0,5):
	for j in range(1,i+1):
		print("*", end='')
	print()

	

*
**
***
****
>>> for i in range(0,5):
	for j in range(1,i+1):
		print("*", end='-------------------')
	print()

	

*-------------------
*-------------------*-------------------
*-------------------*-------------------*-------------------
*-------------------*-------------------*-------------------*-------------------
>>> for i in range(6,0):
	for j in range(i,1):
		print("*", end='')
	print()

	
>>> a = [6,5,4,3,2,1,0]
>>> for i in a:
	for j in range(i,1):
		print("*", end='')
	print()

	






*
>>> for i in range(6,0):
	print(i)

	
>>> for i in reversed(range(0,6)):
	print(i)

	
5
4
3
2
1
0
>>> for i in reversed(range(0,6)):
	for j in range(i,i+1):
		print("*", end='')
	print()

	
*
*
*
*
*
*
>>> for i in reversed(range(0,6)):
	for j in range(1,i+1):
		print("*", end='')
	print()

	
*****
****
***
**
*

>>> a
[6, 5, 4, 3, 2, 1, 0]
>>> for i in a:
	for j in range(1,i+1):
		print("*", end='')
	print()

	
******
*****
****
***
**
*

>>> def func1():
	a = "Hello"
	print(a)

	
>>> func1()
Hello
>>> a
[6, 5, 4, 3, 2, 1, 0]
>>> def func1():
	global a
	a = "Hello"
	print(a)

	
>>> a
[6, 5, 4, 3, 2, 1, 0]
>>> func1()
Hello
>>> a
'Hello'
>>> global a = [6, 5, 4, 3, 2, 1, 0]
SyntaxError: invalid syntax
>>> global a
>>> a = [6, 5, 4, 3, 2, 1, 0]
>>> def func1():
	a = "Hello"
	print(a)

	
>>> func1()
Hello
>>> def func1():
	print(a)
	a = "Hello"
	print(a)

	
>>> func1()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    func1()
  File "<pyshell#62>", line 2, in func1
    print(a)
UnboundLocalError: local variable 'a' referenced before assignment
>>> global a
>>> a = [6, 5, 4, 3, 2, 1, 0]
>>> def func1():
	print(a)
	a = "Hello"
	print(a)

	
>>> func1()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    func1()
  File "<pyshell#67>", line 2, in func1
    print(a)
UnboundLocalError: local variable 'a' referenced before assignment
>>> def func1():
	print(a)

	
>>> func1()
[6, 5, 4, 3, 2, 1, 0]
>>> def func1():
	print(a)
	def func2():		
		a = "Hello"
		print(a)
	func2()

	
>>> func1()
[6, 5, 4, 3, 2, 1, 0]
Hello
>>> a
[6, 5, 4, 3, 2, 1, 0]
>>> def func1():
	print(global a)
	a = "Hello"
	print(a)
	
SyntaxError: invalid syntax
>>> 
>>> def func1():
	print(a)
	global a
	a = "Hello"
	print(a)
	
SyntaxError: name 'a' is used prior to global declaration
>>> def func1():
	print(a)
	print(a)

	
>>> func1()
[6, 5, 4, 3, 2, 1, 0]
[6, 5, 4, 3, 2, 1, 0]
>>> def func1():
	global a
	a = "Hello"
	print(a)

	
>>> func1()
Hello
>>> a
'Hello'
>>> import pygame
>>> pygame.init()
(6, 0)
>>> 

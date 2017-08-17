Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello world")
Hello world
>>> a = 10
>>> type(a)
<class 'int'>
>>> a = "Hello"
>>> type(a)
<class 'str'>
>>> a = 10
>>> b = 20
>>> a + b
30
>>> a-b
-10
>>> a/b
0.5
>>> a*b
200
>>> a**b
100000000000000000000
>>> a**2
100
>>> a = 12
>>> b = 11
>>> a/b
1.0909090909090908
>>> a//b
1
>>> import math
>>> math.ceil(a/b)
2
>>> 
 RESTART: E:/BMPL_Batches/Aug_2017/Regular/Python/Python_11-1/CorePython/01-PythonBasics/01-PythonSyntax.py 
30
>>> 
 RESTART: E:/BMPL_Batches/Aug_2017/Regular/Python/Python_11-1/CorePython/01-PythonBasics/01-PythonSyntax.py 
30
-10
>>> 
 RESTART: E:/BMPL_Batches/Aug_2017/Regular/Python/Python_11-1/CorePython/01-PythonBasics/01-PythonSyntax.py 
30
-10
0.5
0
200
100000000000000000000
>>> 
 RESTART: E:/BMPL_Batches/Aug_2017/Regular/Python/Python_11-1/CorePython/01-PythonBasics/01-PythonSyntax.py 
30
-10
0.5
0
200
100000000000000000000
True
>>> a = {"id" : 1, "Name" : "Ram"}
>>> a
{'id': 1, 'Name': 'Ram'}
>>> a = [1,"Hi",1.5,True]
>>> a
[1, 'Hi', 1.5, True]
>>> print(a)
[1, 'Hi', 1.5, True]
>>> for i in a:
	print(i)

	
1
Hi
1.5
True
>>> for i in a:
	print(i, end="")

	
1Hi1.5True
>>> for i in a:
	print(i, end="----")

	
1----Hi----1.5----True----
>>> class A:
	pass

>>> a = A()
>>> del a
>>> 

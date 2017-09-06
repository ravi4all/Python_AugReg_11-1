Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> file = open('demo.txt', 'r')
>>> data = file.read()
>>> data
'Hello this is python'
>>> print(data)
Hello this is python
>>> data
'Hello this is python'
>>> data[-1]
'n'
>>> data[1:10]
'ello this'
>>> 'is' in data
True
>>> data.replace('Hello', 'Bye')
'Bye this is python'
>>> data
'Hello this is python'
>>> data.count('is')
2
>>> type(data)
<class 'str'>
>>> type(file.read())
<class 'str'>
>>> type(read())
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    type(read())
NameError: name 'read' is not defined
>>> def name():
	pass

>>> type(name)
<class 'function'>
>>> data.count('a')
0
>>> data.count('e')
1
>>> data.count('i')
2
>>> data.count('o')
2
>>> data.count('u')
0
>>> a = ['a', 'e', 'i', 'o', 'u']
>>> for i in data:
	print(data.count(i))

	
1
1
2
2
2
3
2
2
2
2
3
2
2
3
1
1
2
2
2
1
>>> for i in a:
	print(data.count(i))

	
0
1
2
2
0
>>> for i in a:
	print(sum(data.count(i)))

	
Traceback (most recent call last):
  File "<pyshell#32>", line 2, in <module>
    print(sum(data.count(i)))
TypeError: 'int' object is not iterable
>>> x = []
>>> for i in a:
	x.append(data.count(i))
	print(sum(x))

	
0
1
3
5
5
>>> for i in a:
	x.append(data.count(i))

	
>>> print(sum(x))
10
>>> x
[0, 1, 2, 2, 0, 0, 1, 2, 2, 0]
>>> for i in a:
	x.append(data.count(i))

	
>>> x
[0, 1, 2, 2, 0, 0, 1, 2, 2, 0, 0, 1, 2, 2, 0]
>>> x = []
>>> for i in a:
	x.append(data.count(i))

	
>>> x
[0, 1, 2, 2, 0]
>>> sum(x)
5
>>> 

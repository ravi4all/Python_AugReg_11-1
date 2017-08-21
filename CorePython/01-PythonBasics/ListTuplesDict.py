Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> -17%3
1
>>> -17.5%3
0.5
>>> -21%3
0
>>> 21%-3
0
>>> -21%-3
0
>>> -16%3
2
>>> -16/5
-3.2
>>> a = [1,2,3,4,5,6,"Hello","Hi",10.5,True]
>>> a[0]
1
>>> a[-1]
True
>>> a[5]
6
>>> a[0] = "Bye"
>>> a
['Bye', 2, 3, 4, 5, 6, 'Hello', 'Hi', 10.5, True]
>>> a[::-1]
[True, 10.5, 'Hi', 'Hello', 6, 5, 4, 3, 2, 'Bye']
>>> a = []
>>> a.append("Hi",2,10.5)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.append("Hi",2,10.5)
TypeError: append() takes exactly one argument (3 given)
>>> a.append(["Hi",2,10.5])
>>> a
[['Hi', 2, 10.5]]
>>> a = []
>>> a.append(0)
>>> a.append(2)
>>> a
[0, 2]
>>> a= [1,2,3,4,5,6,7]
>>> print(a)
[1, 2, 3, 4, 5, 6, 7]
>>> def func():
	return 1,2,3,4,5

>>> a = func()
>>> a
(1, 2, 3, 4, 5)
>>> a= [1,2,3,4,5,6,7]
>>> for i in a:
	print(i)

	
1
2
3
4
5
6
7
>>> b = []
>>> for i in a:
	if i %2 == 0:
		b.append(i)
	print(b)

	
[]
[2]
[2]
[2, 4]
[2, 4]
[2, 4, 6]
[2, 4, 6]
>>> for i in range(50):
	if i %2 == 0:
		b.append(i)
	print(b)

	
[2, 4, 6, 0]
[2, 4, 6, 0]
[2, 4, 6, 0, 2]
[2, 4, 6, 0, 2]
[2, 4, 6, 0, 2, 4]
[2, 4, 6, 0, 2, 4]
[2, 4, 6, 0, 2, 4, 6]
[2, 4, 6, 0, 2, 4, 6]
[2, 4, 6, 0, 2, 4, 6, 8]
[2, 4, 6, 0, 2, 4, 6, 8]
[2, 4, 6, 0, 2, 4, 6, 8, 10]
[2, 4, 6, 0, 2, 4, 6, 8, 10]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> for i in range(50):
	if i %2 == 0:
		b.append(i)
print(b)
SyntaxError: invalid syntax
>>> for i in range(50):
	if i %2 == 0:
		b.append(i)

		
>>> print(b)
[2, 4, 6, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> x = [i for i in range(50) if i%2 ==0]
>>> x
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> a = [1,2,3,4,5,6,"Hello","Hi",10.5,True]
>>> a.pop()
True
>>> a
[1, 2, 3, 4, 5, 6, 'Hello', 'Hi', 10.5]
>>> a.pop(4)
5
>>> a.remove('Hello')
>>> a
[1, 2, 3, 4, 6, 'Hi', 10.5]
>>> b = ['a','e','i','o','u']
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 6, 'Hi', 10.5, 'a', 'e', 'i', 'o', 'u']
>>> c = [1,2,3,4,5]
>>> a+c
[1, 2, 3, 4, 6, 'Hi', 10.5, 'a', 'e', 'i', 'o', 'u', 1, 2, 3, 4, 5]
>>> a.insert(0,"Bye")
>>> a
['Bye', 1, 2, 3, 4, 6, 'Hi', 10.5, 'a', 'e', 'i', 'o', 'u']
>>> a[3] = "Python"
>>> a
['Bye', 1, 2, 'Python', 4, 6, 'Hi', 10.5, 'a', 'e', 'i', 'o', 'u']
>>> a.index('Python')
3
>>> a[3][3]
'h'
>>> a[3][1:] = "rogramming"
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a[3][1:] = "rogramming"
TypeError: 'str' object does not support item assignment
>>> a[3][1:]
'ython'
>>> a = ['Bye', 1, 2, ['Python', 4, 6,], 'Hi', 10.5, ['a', 'e', 'i', 'o', 'u']]
>>> a[-1]
['a', 'e', 'i', 'o', 'u']
>>> a[-1][0]
'a'
>>> a[-1][0] = 'x'
>>> a
['Bye', 1, 2, ['Python', 4, 6], 'Hi', 10.5, ['x', 'e', 'i', 'o', 'u']]
>>> a[-1][0] = 'python'
>>> a
['Bye', 1, 2, ['Python', 4, 6], 'Hi', 10.5, ['python', 'e', 'i', 'o', 'u']]
>>> a = [1,2,3,4,5]
>>> b = a
>>> b
[1, 2, 3, 4, 5]
>>> b[0] = "Hi"
>>> b
['Hi', 2, 3, 4, 5]
>>> a
['Hi', 2, 3, 4, 5]
>>> a = [1,2,3,4,5]
>>> b = a.copy()
>>> b[0] = "Hi"
>>> b
['Hi', 2, 3, 4, 5]
>>> a
[1, 2, 3, 4, 5]
>>> sum(a)
15
>>> a = [2,21,13,14,52,23,11,0,1]
>>> a
[2, 21, 13, 14, 52, 23, 11, 0, 1]
>>> sorted(a)
[0, 1, 2, 11, 13, 14, 21, 23, 52]
>>> sorted(a, reverse=True)
[52, 23, 21, 14, 13, 11, 2, 1, 0]
>>> a
[2, 21, 13, 14, 52, 23, 11, 0, 1]
>>> b = ['Ram','Raman','Aman','Ashish','Akash','Sumit','Shyam']
>>> sorted(b)
['Akash', 'Aman', 'Ashish', 'Ram', 'Raman', 'Shyam', 'Sumit']
>>> a
[2, 21, 13, 14, 52, 23, 11, 0, 1]
>>> b
['Ram', 'Raman', 'Aman', 'Ashish', 'Akash', 'Sumit', 'Shyam']
>>> a = [2,21,13,14,11,0,1]
>>> len(a)
7
>>> len(b)
7
>>> x = zip(a,b)
>>> x
<zip object at 0x033D00D0>
>>> x = list(zip(a,b))
>>> x
[(2, 'Ram'), (21, 'Raman'), (13, 'Aman'), (14, 'Ashish'), (11, 'Akash'), (0, 'Sumit'), (1, 'Shyam')]
>>> for i in x:
	print(i)

	
(2, 'Ram')
(21, 'Raman')
(13, 'Aman')
(14, 'Ashish')
(11, 'Akash')
(0, 'Sumit')
(1, 'Shyam')
>>> x
[(2, 'Ram'), (21, 'Raman'), (13, 'Aman'), (14, 'Ashish'), (11, 'Akash'), (0, 'Sumit'), (1, 'Shyam')]
>>> x[0]
(2, 'Ram')
>>> x[1]
(21, 'Raman')
>>> x[0][1]
'Ram'
>>> x[0]['Ram']
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    x[0]['Ram']
TypeError: tuple indices must be integers or slices, not str
>>> l = x[0]
>>> l
(2, 'Ram')
>>> l['Ram']
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    l['Ram']
TypeError: tuple indices must be integers or slices, not str
>>> a
[2, 21, 13, 14, 11, 0, 1]
>>> a.remove(21)
>>> a
[2, 13, 14, 11, 0, 1]
>>> a.remove()
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    a.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> a.remove(11111)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    a.remove(11111)
ValueError: list.remove(x): x not in list
>>> a
[2, 13, 14, 11, 0, 1]
>>> s = 11
>>> s in a
True
>>> a = "10"
>>> b = 10
>>> a is b
False
>>> a == b
False
>>> a = [1,2,2,3,4]
>>> b = [4,5,2,3,4]
>>> a is b
False
>>> a == b
False
>>> c = a
>>> c is b
False
>>> c is a
True
>>> c == a
True
>>> i = b[:]
>>> i
[4, 5, 2, 3, 4]
>>> i is b
False
>>> i == b
True
>>> a = [1,2,3,4,["Hi","Hello","Bye"], 11,12,13]
>>> b = a.copy()
>>> b[4][0] = "Python"
>>> a
[1, 2, 3, 4, ['Python', 'Hello', 'Bye'], 11, 12, 13]
>>> b
[1, 2, 3, 4, ['Python', 'Hello', 'Bye'], 11, 12, 13]
>>> b[1] = "Ok"
>>> b
[1, 'Ok', 3, 4, ['Python', 'Hello', 'Bye'], 11, 12, 13]
>>> a
[1, 2, 3, 4, ['Python', 'Hello', 'Bye'], 11, 12, 13]
>>> b = a[:]
>>> b
[1, 2, 3, 4, ['Python', 'Hello', 'Bye'], 11, 12, 13]
>>> a
[1, 2, 3, 4, ['Python', 'Hello', 'Bye'], 11, 12, 13]
>>> b[0] = "Ok"
>>> b
['Ok', 2, 3, 4, ['Python', 'Hello', 'Bye'], 11, 12, 13]
>>> a
[1, 2, 3, 4, ['Python', 'Hello', 'Bye'], 11, 12, 13]
>>> b[4][0] = "Hi"
>>> b
['Ok', 2, 3, 4, ['Hi', 'Hello', 'Bye'], 11, 12, 13]
>>> a
[1, 2, 3, 4, ['Hi', 'Hello', 'Bye'], 11, 12, 13]
>>> import copy
>>> b = copy.deepcopy(a)
>>> b
[1, 2, 3, 4, ['Hi', 'Hello', 'Bye'], 11, 12, 13]
>>> a
[1, 2, 3, 4, ['Hi', 'Hello', 'Bye'], 11, 12, 13]
>>> b[4][0] = "Something"
>>> b
[1, 2, 3, 4, ['Something', 'Hello', 'Bye'], 11, 12, 13]
>>> a
[1, 2, 3, 4, ['Hi', 'Hello', 'Bye'], 11, 12, 13]
>>> a.clear()
>>> a
[]
>>> a = 10,12,13,14
>>> a
(10, 12, 13, 14)
>>> type(a)
<class 'tuple'>
>>> a = (10,12,13,14)
>>> a
(10, 12, 13, 14)
>>> a = 10,12,13,14,
>>> a
(10, 12, 13, 14)
>>> a = ,10,12,13,14,
SyntaxError: invalid syntax
>>> a = 10,,12,13,14,
SyntaxError: invalid syntax
>>> a = 10,12,13,14,
>>> a
(10, 12, 13, 14)
>>> a[0]
10
>>> a = (1,2,3,4,(5,6,7,8))
>>> a
(1, 2, 3, 4, (5, 6, 7, 8))
>>> a[0]
1
>>> a[-1]
(5, 6, 7, 8)
>>> a[0] = "Hello"
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    a[0] = "Hello"
TypeError: 'tuple' object does not support item assignment
>>> a.index(1)
0
>>> a.count(1)
1
>>> a = [1,2,3,4,["Hi","Hello","Bye"], 11,12,13]
>>> a.count(1)
1
>>> a = [2,2,2,3,4,5]
>>> a.count(2)
3
>>> a.count*(2)
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    a.count*(2)
TypeError: unsupported operand type(s) for *: 'builtin_function_or_method' and 'int'
>>> a.count(*)
SyntaxError: invalid syntax
>>> import set
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    import set
ModuleNotFoundError: No module named 'set'
>>> import sets
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    import sets
ModuleNotFoundError: No module named 'sets'
>>> a = {"id":1,"name":"Ram","age":12}
>>> a
{'id': 1, 'name': 'Ram', 'age': 12}
>>> for i in a:
	print(i)

	
id
name
age
>>> for i in a.items():
	print(i)

	
('id', 1)
('name', 'Ram')
('age', 12)
>>> for i in a.values():
	print(i)

	
1
Ram
12
>>> a.fromkeys('id')
{'i': None, 'd': None}
>>> a.fromkeys('i')
{'i': None}
>>> x = {'a':1, "a":2,"a":3}
>>> x.fromkeys(a)
{'id': None, 'name': None, 'age': None}
>>> x.fromkeys('a')
{'a': None}
>>> a
{'id': 1, 'name': 'Ram', 'age': 12}
>>> for i in a:
	print("The id is {} and name is {}".format(i.id, i.name))

	
Traceback (most recent call last):
  File "<pyshell#208>", line 2, in <module>
    print("The id is {} and name is {}".format(i.id, i.name))
AttributeError: 'str' object has no attribute 'id'
>>> for i in a:
	print("The id is {} and name is {}".format(a['id'], a['name']))

	
The id is 1 and name is Ram
The id is 1 and name is Ram
The id is 1 and name is Ram
>>> a.values()
dict_values([1, 'Ram', 12])
>>> a.keys()
dict_keys(['id', 'name', 'age'])
>>> a['id'] = 2
>>> a
{'id': 2, 'name': 'Ram', 'age': 12}
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> a.pop(0)
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    a.pop(0)
KeyError: 0
>>> a.pop('id')
2
>>> 
>>> a
{'name': 'Ram', 'age': 12}
>>> 

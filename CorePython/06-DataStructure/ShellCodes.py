Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [1,2,3,4,5,6]
>>> a
[1, 2, 3, 4, 5, 6]
>>> a = (1,2,3,4,5,6)
>>> a
(1, 2, 3, 4, 5, 6)
>>> type(a)
<class 'tuple'>
>>> a[2]
3
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.count()
TypeError: count() takes exactly one argument (0 given)
>>> a.count(1)
1
>>> a = (1,2,3,4,5,1,2,3,4,5)
>>> a.count(2)
2
>>> a.index(1)
0
>>> i = [1,2,3,4,5,6]
>>> i[1] = 'Hello'
>>> i
[1, 'Hello', 3, 4, 5, 6]
>>> a[1] = "Hello"
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a[1] = "Hello"
TypeError: 'tuple' object does not support item assignment
>>> a = ('Hi',1,2,3,7.6,'Hello')
>>> a[1] = 10.5
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a[1] = 10.5
TypeError: 'tuple' object does not support item assignment
>>> d = {'id':101,'name':'Ram','Age':20}
>>> for i in d:
	print(i)

id
name
Age
>>> d.keys()
dict_keys(['id', 'name', 'Age'])
>>> d.values()
dict_values([101, 'Ram', 20])
>>> for i in d.items():
	print(i)

('id', 101)
('name', 'Ram')
('Age', 20)
>>> d['id'] = 102
>>> d
{'id': 102, 'name': 'Ram', 'Age': 20}
>>> d.update()
>>> d
{'id': 102, 'name': 'Ram', 'Age': 20}
>>> 

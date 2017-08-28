Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = lambda : print("Anonymous Function")
>>> a
<function <lambda> at 0x000001A16E7A66A8>
>>> a()
Anonymous Function
>>> a = [{'Name': 'Nokia', 'Price': '23000', 'Description': 'Nokia Lumia'}, {'Name': 'Motorola', 'Price': '15000', 'Description': 'MotoG'}, {'Name': 'Apple', 'Price': 'Iphone', 'Description': '23000'}]
>>> sorted(a, key=lambda x : x['price'])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    sorted(a, key=lambda x : x['price'])
  File "<pyshell#4>", line 1, in <lambda>
    sorted(a, key=lambda x : x['price'])
KeyError: 'price'
>>> sorted(a, key=lambda x : x['Price'])
[{'Name': 'Motorola', 'Price': '15000', 'Description': 'MotoG'}, {'Name': 'Nokia', 'Price': '23000', 'Description': 'Nokia Lumia'}, {'Name': 'Apple', 'Price': 'Iphone', 'Description': '23000'}]
>>> sorted(a, key=lambda : ['Price'])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    sorted(a, key=lambda : ['Price'])
TypeError: <lambda>() takes 0 positional arguments but 1 was given
>>> sorted(a, key=lambda : ['Name'])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    sorted(a, key=lambda : ['Name'])
TypeError: <lambda>() takes 0 positional arguments but 1 was given
>>> sorted(a, key=lambda x : x['Name'])
[{'Name': 'Apple', 'Price': 'Iphone', 'Description': '23000'}, {'Name': 'Motorola', 'Price': '15000', 'Description': 'MotoG'}, {'Name': 'Nokia', 'Price': '23000', 'Description': 'Nokia Lumia'}]
>>> 

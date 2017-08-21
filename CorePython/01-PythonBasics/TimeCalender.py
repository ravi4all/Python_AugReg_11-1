Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import time
>>> from datetime import datetim
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    from datetime import datetim
ImportError: cannot import name 'datetim'
>>> from datetime import datetime
>>> now = datetime.now()
>>> now
datetime.datetime(2017, 8, 21, 12, 11, 6, 400060)
>>> print(now)
2017-08-21 12:11:06.400060
>>> datetime.strftime("%H")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    datetime.strftime("%H")
TypeError: descriptor 'strftime' requires a 'datetime.date' object but received a 'str'
>>> datetime.strftime(%H)
SyntaxError: invalid syntax
>>> now.strftime("%H")
'12'
>>> now.strftime("%HM")
'12M'
>>> now.strftime("%H:%M:%S")
'12:11:06'
>>> now.month()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    now.month()
TypeError: 'int' object is not callable
>>> now.month
8
>>> now.year
2017
>>> now.date
<built-in method date of datetime.datetime object at 0x033F44D0>
>>> print(now.date)
<built-in method date of datetime.datetime object at 0x033F44D0>
>>> now.date()
datetime.date(2017, 8, 21)
>>> now.day
21
>>> x = now.strftime("%H")
>>> x += 1
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x += 1
TypeError: must be str, not int
>>> x = int(now.strftime("%H"))
>>> x += 1
>>> x
13
>>> import calendar
>>> calendar.month
<bound method TextCalendar.formatmonth of <calendar.TextCalendar object at 0x0345B830>>
>>> calendar.month()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    calendar.month()
TypeError: formatmonth() missing 2 required positional arguments: 'theyear' and 'themonth'
>>> calendar.month(2017,8)
'    August 2017\nMo Tu We Th Fr Sa Su\n    1  2  3  4  5  6\n 7  8  9 10 11 12 13\n14 15 16 17 18 19 20\n21 22 23 24 25 26 27\n28 29 30 31\n'
>>> print(calendar.month(2017,8))
    August 2017
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31

>>> print(calendar.month(2021,8))
    August 2021
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31

>>> 

Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello  "Ravi"")
SyntaxError: invalid syntax
>>> print("Hello" + "Ravi")
HelloRavi
>>> print('Hello "Ravi" ')
Hello "Ravi" 
>>> print("Hello 'Ravi' ")
Hello 'Ravi' 
>>> print(""Hello"")
SyntaxError: invalid syntax
>>> print("'Hello'")
'Hello'
>>> "Hello" + "World"
'HelloWorld'
>>> "Hello"
'Hello'
>>> '"Hello"'
'"Hello"'
>>> print("Hello \n World")
Hello 
 World
>>> print("Hello \\n World")
Hello \n World
>>> print(r"Hello \n World")
Hello \n World
>>> a = "Hello world"
>>> len(a)
11
>>> a[0:4]
'Hell'
>>> a[:4]
'Hell'
>>> a[4:]
'o world'
>>> a[-1]
'd'
>>> a[::-1]
'dlrow olleH'
>>> a[:-1]
'Hello worl'
>>> a.
SyntaxError: invalid syntax
>>> a.capitalize()
'Hello world'
>>> a.capitalize
<built-in method capitalize of str object at 0x0318D0E8>
>>> a.capitalize()
'Hello world'
>>> a.casefold()
'hello world'
>>> a.upper()
'HELLO WORLD'
>>> a.lower()
'hello world'
>>> a[0]
'H'
>>> help()

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> chartat
No Python documentation found for 'chartat'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> capitalize()
No Python documentation found for 'capitalize()'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> capitaliza
No Python documentation found for 'capitaliza'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> capitalize
No Python documentation found for 'capitalize'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> capitalize()
No Python documentation found for 'capitalize()'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> help(capitalize)
No Python documentation found for 'help(capitalize)'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> help("Hello")
No Python documentation found for 'help(Hello)'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> help(capitalize)
No Python documentation found for 'help(capitalize)'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> str
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(...)
 |      S.__format__(format_spec) -> str
 |      
 |      Return a formatted version of S as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(...)
 |      S.capitalize() -> str
 |      
 |      Return a capitalized version of S, i.e. make the first character
 |      have upper case and the rest lower case.
 |  
 |  casefold(...)
 |      S.casefold() -> str
 |      
 |      Return a version of S suitable for caseless comparisons.
 |  
 |  center(...)
 |      S.center(width[, fillchar]) -> str
 |      
 |      Return S centered in a string of length width. Padding is
 |      done using the specified fill character (default is a space)
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(...)
 |      S.encode(encoding='utf-8', errors='strict') -> bytes
 |      
 |      Encode S using the codec registered for encoding. Default encoding
 |      is 'utf-8'. errors may be given to set a different error
 |      handling scheme. Default is 'strict' meaning that encoding errors raise
 |      a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
 |      'xmlcharrefreplace' as well as any other name registered with
 |      codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(...)
 |      S.expandtabs(tabsize=8) -> str
 |      
 |      Return a copy of S where all tab characters are expanded using spaces.
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Like S.find() but raise ValueError when the substring is not found.
 |  
 |  isalnum(...)
 |      S.isalnum() -> bool
 |      
 |      Return True if all characters in S are alphanumeric
 |      and there is at least one character in S, False otherwise.
 |  
 |  isalpha(...)
 |      S.isalpha() -> bool
 |      
 |      Return True if all characters in S are alphabetic
 |      and there is at least one character in S, False otherwise.
 |  
 |  isdecimal(...)
 |      S.isdecimal() -> bool
 |      
 |      Return True if there are only decimal characters in S,
 |      False otherwise.
 |  
 |  isdigit(...)
 |      S.isdigit() -> bool
 |      
 |      Return True if all characters in S are digits
 |      and there is at least one character in S, False otherwise.
 |  
 |  isidentifier(...)
 |      S.isidentifier() -> bool
 |      
 |      Return True if S is a valid identifier according
 |      to the language definition.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers
 |      such as "def" and "class".
 |  
 |  islower(...)
 |      S.islower() -> bool
 |      
 |      Return True if all cased characters in S are lowercase and there is
 |      at least one cased character in S, False otherwise.
 |  
 |  isnumeric(...)
 |      S.isnumeric() -> bool
 |      
 |      Return True if there are only numeric characters in S,
 |      False otherwise.
 |  
 |  isprintable(...)
 |      S.isprintable() -> bool
 |      
 |      Return True if all characters in S are considered
 |      printable in repr() or S is empty, False otherwise.
 |  
 |  isspace(...)
 |      S.isspace() -> bool
 |      
 |      Return True if all characters in S are whitespace
 |      and there is at least one character in S, False otherwise.
 |  
 |  istitle(...)
 |      S.istitle() -> bool
 |      
 |      Return True if S is a titlecased string and there is at least one
 |      character in S, i.e. upper- and titlecase characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |      Return False otherwise.
 |  
 |  isupper(...)
 |      S.isupper() -> bool
 |      
 |      Return True if all cased characters in S are uppercase and there is
 |      at least one cased character in S, False otherwise.
 |  
 |  join(...)
 |      S.join(iterable) -> str
 |      
 |      Return a string which is the concatenation of the strings in the
 |      iterable.  The separator between elements is S.
 |  
 |  ljust(...)
 |      S.ljust(width[, fillchar]) -> str
 |      
 |      Return S left-justified in a Unicode string of length width. Padding is
 |      done using the specified fill character (default is a space).
 |  
 |  lower(...)
 |      S.lower() -> str
 |      
 |      Return a copy of the string S converted to lowercase.
 |  
 |  lstrip(...)
 |      S.lstrip([chars]) -> str
 |      
 |      Return a copy of the string S with leading whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(...)
 |      S.partition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, and return the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, return S and two empty strings.
 |  
 |  replace(...)
 |      S.replace(old, new[, count]) -> str
 |      
 |      Return a copy of S with all occurrences of substring
 |      old replaced by new.  If the optional argument count is
 |      given, only the first count occurrences are replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Like S.rfind() but raise ValueError when the substring is not found.
 |  
 |  rjust(...)
 |      S.rjust(width[, fillchar]) -> str
 |      
 |      Return S right-justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space).
 |  
 |  rpartition(...)
 |      S.rpartition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, starting at the end of S, and return
 |      the part before it, the separator itself, and the part after it.  If the
 |      separator is not found, return two empty strings and S.
 |  
 |  rsplit(...)
 |      S.rsplit(sep=None, maxsplit=-1) -> list of strings
 |      
 |      Return a list of the words in S, using sep as the
 |      delimiter string, starting at the end of the string and
 |      working to the front.  If maxsplit is given, at most maxsplit
 |      splits are done. If sep is not specified, any whitespace string
 |      is a separator.
 |  
 |  rstrip(...)
 |      S.rstrip([chars]) -> str
 |      
 |      Return a copy of the string S with trailing whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(...)
 |      S.split(sep=None, maxsplit=-1) -> list of strings
 |      
 |      Return a list of the words in S, using sep as the
 |      delimiter string.  If maxsplit is given, at most maxsplit
 |      splits are done. If sep is not specified or is None, any
 |      whitespace string is a separator and empty strings are
 |      removed from the result.
 |  
 |  splitlines(...)
 |      S.splitlines([keepends]) -> list of strings
 |      
 |      Return a list of the lines in S, breaking at line boundaries.
 |      Line breaks are not included in the resulting list unless keepends
 |      is given and true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(...)
 |      S.strip([chars]) -> str
 |      
 |      Return a copy of the string S with leading and trailing
 |      whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(...)
 |      S.swapcase() -> str
 |      
 |      Return a copy of S with uppercase characters converted to lowercase
 |      and vice versa.
 |  
 |  title(...)
 |      S.title() -> str
 |      
 |      Return a titlecased version of S, i.e. words start with title case
 |      characters, all remaining cased characters have lower case.
 |  
 |  translate(...)
 |      S.translate(table) -> str
 |      
 |      Return a copy of the string S in which each character has been mapped
 |      through the given translation table. The table must implement
 |      lookup/indexing via __getitem__, for instance a dictionary or list,
 |      mapping Unicode ordinals to Unicode ordinals, strings, or None. If
 |      this operation raises LookupError, the character is left untouched.
 |      Characters mapped to None are deleted.
 |  
 |  upper(...)
 |      S.upper() -> str
 |      
 |      Return a copy of S converted to uppercase.
 |  
 |  zfill(...)
 |      S.zfill(width) -> str
 |      
 |      Pad a numeric string S with zeros on the left, to fill a field
 |      of the specified width. The string S is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

help> exit
Help on Quitter in module _sitebuiltins object:

exit = class Quitter(builtins.object)
 |  Methods defined here:
 |  
 |  __call__(self, code=None)
 |      Call self as a function.
 |  
 |  __init__(self, name, eof)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

help> exit()
No Python documentation found for 'exit()'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> a = "Hello this is python programming"
>>> a.find("o")
4
>>> a.find("Hello")
0
>>> a.find("this")
6
>>> a.find("p")
14
>>> a.split()
['Hello', 'this', 'is', 'python', 'programming']
>>> b = a.split()
>>> b
['Hello', 'this', 'is', 'python', 'programming']
>>> b.strip("[]")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    b.strip("[]")
AttributeError: 'list' object has no attribute 'strip'
>>> str(b.strip("[]"))
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    str(b.strip("[]"))
AttributeError: 'list' object has no attribute 'strip'
>>> x = str(b)
>>> x
"['Hello', 'this', 'is', 'python', 'programming']"
>>> x.strip("[]")
"'Hello', 'this', 'is', 'python', 'programming'"
>>> a
'Hello this is python programming'
>>> a[0:10]
'Hello this'
>>> a[0:100]
'Hello this is python programming'
>>> a[100]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a[100]
IndexError: string index out of range
>>> a[0] = "Bye"
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a[0] = "Bye"
TypeError: 'str' object does not support item assignment
>>> a.replace("Hello", "Bye")
'Bye this is python programming'
>>> a
'Hello this is python programming'
>>> import turtle
>>> turt = turtle.Turtle()
>>> turt.showturtle()
>>> turt.forward(100)
>>> turt.left(90)
>>> turt.forward(100)
>>> turt.reset()
>>> for i in range(4):
	turt.forward(100)
	turt.left(90)

	
>>> turt.reset()
>>> for i in range(20):
	turt.forward(100 + i*5)
	turt.left(90)

	
>>> for i in range(20):
	turt.forward(i*5)
	turt.left(90)

	
>>> turt.reset()
>>> for i in range(50):
	turt.forward(i*5)
	turt.left(90)

	

>>> turt.speed(1)
>>> turt.reset()
>>> turt.speed(1)
>>> for i in range(50):
	turt.forward(i*5)
	turt.left(90)

	
>>> turt.reset()
>>> turt.speed(10)
>>> for i in range(50):
	turt.forward(i*5)
	turt.left(90)

	
>>> turt.reset()
>>> for i in range(20):
	turt.circle(i*5)

	

>>> turt.reset()
>>> turt.speed(10)
>>> for i in range(20):
	turt.circle(i*5)

	
Traceback (most recent call last):
  File "<pyshell#83>", line 2, in <module>
    turt.circle(i*5)
  File "C:\Python36-32\lib\turtle.py", line 1993, in circle
    self._rotate(w)
  File "C:\Python36-32\lib\turtle.py", line 3278, in _rotate
    self._update()
  File "C:\Python36-32\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python36-32\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python36-32\lib\tkinter\__init__.py", line 741, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> turt.reset()
>>> turt.speed(10)
>>> for i in range(20):
	turt.circle(i*5)
	turt.left(50)

	
>>> turt.color(255,0,0)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    turt.color(255,0,0)
  File "C:\Python36-32\lib\turtle.py", line 2216, in color
    pcolor = self._colorstr(pcolor)
  File "C:\Python36-32\lib\turtle.py", line 2696, in _colorstr
    return self.screen._colorstr(args)
  File "C:\Python36-32\lib\turtle.py", line 1166, in _colorstr
    raise TurtleGraphicsError("bad color sequence: %s" % str(color))
turtle.TurtleGraphicsError: bad color sequence: (255, 0, 0)
>>> turt.color('red')
>>> turt.reset()
>>> for i in range(20):
	turt.circle(i*5)
	turt.left(50)

	
Traceback (most recent call last):
  File "<pyshell#93>", line 2, in <module>
    turt.circle(i*5)
  File "C:\Python36-32\lib\turtle.py", line 1990, in circle
    self.speed(speed)
  File "C:\Python36-32\lib\turtle.py", line 2174, in speed
    self.pen(speed=speed)
  File "C:\Python36-32\lib\turtle.py", line 2459, in pen
    self._update()
  File "C:\Python36-32\lib\turtle.py", line 2662, in _update
    screen._update()                  # TurtleScreenBase
  File "C:\Python36-32\lib\turtle.py", line 562, in _update
    self.cv.update()
  File "C:\Python36-32\lib\tkinter\__init__.py", line 1171, in update
    self.tk.call('update')
KeyboardInterrupt
>>> turt.reset()
>>> turt.shape("turtle")
>>> for i in range(8):
	fred.forward(120)
	fred.left(225)

	
Traceback (most recent call last):
  File "<pyshell#97>", line 2, in <module>
    fred.forward(120)
NameError: name 'fred' is not defined
>>> for i in range(8):
	turt.forward(120)
	turt.left(225)

	
>>> turt.reset()
>>> turt.shape("turtle")
>>> for i in range(50):
	turt.circle(100)
	turt.left(10)

	
Traceback (most recent call last):
  File "<pyshell#103>", line 2, in <module>
    turt.circle(100)
  File "C:\Python36-32\lib\turtle.py", line 1990, in circle
    self.speed(speed)
  File "C:\Python36-32\lib\turtle.py", line 2174, in speed
    self.pen(speed=speed)
  File "C:\Python36-32\lib\turtle.py", line 2459, in pen
    self._update()
  File "C:\Python36-32\lib\turtle.py", line 2662, in _update
    screen._update()                  # TurtleScreenBase
  File "C:\Python36-32\lib\turtle.py", line 562, in _update
    self.cv.update()
  File "C:\Python36-32\lib\tkinter\__init__.py", line 1171, in update
    self.tk.call('update')
KeyboardInterrupt
>>> turt.reset()
>>> turt.color("red")
>>> a = ["red","blue","green","cyan","yellow"]
>>> import random
>>> turt.speed(0)
>>> for i in range(50):
	col = random.choice(a)
	turt.color(col)
	turt.circle(100)
	turt.left(10)

	
>>> turt.reset()
>>> for i in range(50):
	turt.circle(3*i)
	turt.left(10)

	
Traceback (most recent call last):
  File "<pyshell#114>", line 2, in <module>
    turt.circle(3*i)
  File "C:\Python36-32\lib\turtle.py", line 1993, in circle
    self._rotate(w)
  File "C:\Python36-32\lib\turtle.py", line 3278, in _rotate
    self._update()
  File "C:\Python36-32\lib\turtle.py", line 2660, in _update
    self._update_data()
  File "C:\Python36-32\lib\turtle.py", line 2651, in _update_data
    self._pencolor, self._pensize)
  File "C:\Python36-32\lib\turtle.py", line 545, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Python36-32\lib\tkinter\__init__.py", line 2463, in coords
    self.tk.call((self._w, 'coords') + args))]
KeyboardInterrupt
>>> turt.reset()
>>> turt.speed(0)
>>> for i in range(50):
	turt.circle(3*i)
	turt.left(10)

	
>>> turt.reset()
>>> turt.speed(0)
>>> for i in range(100):
	col = random.choice(a)
	turt.color(col)
	turt.circle(3*i)
	turt.left(10)

	
>>> turt.reset()
>>> turt.speed(0)
>>> for i in range(50):
	col = random.choice(a)
	turt.color(col)
	turt.circle(3*i)
	turt.left(10)

	
>>> fred.reset()
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    fred.reset()
NameError: name 'fred' is not defined
>>> turt.reset()
>>> turt.speed(0)
>>> for i in range(80):
	col = random.choice(a)
	turt.color(col)
	turt.circle(3*i,180)
	turt.left(10)

	
>>> turt.reset()
>>> turt.speed(0)
>>> for i in range(80):
	col = random.choice(a)
	turt.color(col)
	turt.circle(3*i,90)
	turt.left(10)

	
>>> for i in range(80):
	col = random.choice(a)
	turt.color(col)
	turt.circle(3*i)
	turt.left(10)

	
>>> turt.reset()
>>> 

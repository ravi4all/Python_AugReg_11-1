import re

str = "Hello ravi.tyagi@gmail.com we are bmpl_center@gmail.com and email id is ravi.bmpl@bmpl.edu.in"

# x = re.search('[\w]+@+[\w]+', str)

# x = re.search('[\w.-]+@+[\w.-]+', str)

x = re.findall('[\w.-]+@+[\w.-]+', str)

print(x)

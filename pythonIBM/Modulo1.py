print ("Hola mundo")

import sys
print(sys.version_info)

print(type(12))
print(type(12.0))
print(type("hello"))
print(type(True))

a = 6/2
print(type(a))

a = 6//2
print(type(a))

### Espresiones y simbolos
s = 43+60+16+41
r = 50-60
m = 5*5
d = 25/5
df = 25/6
de = 25 // 5

x = 3+2*2
y = (3+2)*2

z = x + y
print (x)
print (y)
print (z)

w = 11//2
print(w)

v = 4
v = v/2
print(v)


# y = 2*x*2-3
y = 2*x*x-3
print(y)

### Formato en cadenas
# String interpolation (f-strings)
name = "Angel"
age = "37"
print(f"My name is {name} \nand I am {age} years old")

# str.format()
name = "Angel"
age = "37"
print("My name is {} \nand I am {} years old".format(name, age))

# % Operator
name = "Angel"
age = "37"
print("My name is %s \nand I am %s years old"% (name, age))

# Additional capabilities
x = 10
y = 20
print(f"The sum of x and y is {x+y}.")


# import os
# Raw String (r’’)
"""regular string"""
regular_string = "C:\new_folder\file.txt"
print("Regular String:", regular_string)

"""raw string"""
raw_string = r"C:\new_folder\file.txt"
print("Raw String:", raw_string)


name = "Michael Jackson"

print(name[0])
print(name[6])
print(name[13])

print(name[-1])
print(name[-15])

print(len(name))

print(name[0:4])
print(name[8:12])

print(name[::2])
print(name[0:5:2])

statement = name + "\t is the best" # \t tabulador o espacio en la misma linea
statement

print(statement)

print( 3 * name)
print( 3 * "\t{}".format(name))
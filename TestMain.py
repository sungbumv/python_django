# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

if 5 < 2:
    print("Hello, world")
print("=======================================")

x = 5
y = "string"
print(x)
print(y)

print("=======================================")

x = 4
x = "sally"
print(x)

print("=======================================")
x = str(3)
y = int(3)
z = float(3)
print(x,y,z)

print("=======================================")

x = 5
y = "John"
print(type(x))
print(type(y))

print("=======================================")

x = "John"
print(x)
x = 'John'
print(x)

print("=======================================")

a = 4
print(a)
A = "Sally"
print(A)

print("=======================================")

x, y, z = "Orange" , "Banana", "Cherry"
print(x)
print(y)
print(z)

print("=======================================")

x=y=z="Orange"
print(x)
print(y)
print(z)

print("=======================================")

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print("=======================================")

x = "output Variables"
print(x)

x = "1번은"
y = "2번과"
z = "같을걸요"
print(x,y,z)

print("=======================================")

x = 5;
y = 10;

print(x + y)


x = 5
y = "John"
print(x,y)

print("=======================================")

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

print("=======================================")
x = 5
print(type(x))
print("=======================================")

x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

print("=======================================")

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
print("=======================================")

x = 1.10
y= 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

print("=======================================")
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

print("=======================================")

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

print("=======================================")

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

print("=======================================")

print(random.randrange(1,10))

print("=======================================")

x = int(1)
y = int(2.8)
z = int("3")

print(x)
print(y)
print(z)

print("=======================================")

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")

print(x)
print(y)
print(z)
print(w)

print("=======================================")

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x)
print(y)
print(z)

print("=======================================")
print("Hello")
print('Hello')

print("=======================================")

a = "Hello"
print(a)

print("=======================================")

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print("=======================================")

b = "Hello, World!"
print(b[2:5])

print("=======================================")


b = "Hello, World!"
print(b[:5])


b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])


a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

print("=======================================")

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

print("=======================================")

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

print("=======================================")

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print("=======================================")

thislist = ["apple", "banana", "cherry"]
print(thislist)

exit()



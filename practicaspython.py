# Test de Print
print ("hola mundo")
print (9999999*10514)
# Strings <srt>
print("Hello World")
print('Hello World')
print("""Hello World""")
print('''Hello World''')
print(type("hello World"))

# Concadenacion
print("bye" + "World")

# Numbers
# Int
print(30)

# Float
print(30.5)

# Boolean
True
False

# List
[10, 20, 30, 40]
["Hello", "Bye", "Adios"]
[]

# Tuples
(10, 20, 30, 40)
()
x = (1,2,3)
y = tuple((1,2,3))
print(dir(x))
print(type(x)) 
print(x[0])
del x
locations = {
    (35.12312, 39.000): "Tokyo",
    (35.12312, 39.050): "New York"
}

# Dictorionies
print(type({
    "name":"Tato",
    "Apellido":"Coffee",
    "Apodo":"Fazt"
}
))
None
product = {
    "name": "Book",
    "quantity": 3,
    "price": 4.99
}
person = {
    "fn": "Tato",
    "ln": "Coffee"
}
print(type(product))
print(dir(person))
print(person.fromkeys())
print(person.items())

del person
print(person)
person.clear()
print(person)

# Variables
name_nick = "Tato"
name = "javier"
print(name, name_nick)

# Encadenados
print(name.replace("javier", "Coffee").upper())

# Print
print(name.upper())
print(name.lower())
print(name.swapcase())
print(name.capitalize())
print(name.replace())
print(name.count())

print(name.startswith("he"))
print(name.endswith("world"))

print(name.split("o"))
print(name.find("z"))

print(len(name))
print(name.index("e"))

print(name.isnumeric())
print(name.isalpha())

print(name[4])

# Concatenar
print("My name is {name}")
print("My name is" + name)
print("My name is (0)".format(name))

# Numbers
# 10
# 10.5
# 3+3
# 3-1
# 2*3
# 2/3
# 2//3
# 2.4*1.4
# 20-10/5*3
age = input("Edad: ")
print(age)
new_age = int() + 5
print(new_age)

# Set
colors = {"r, g, b"}
print(colors)
print("r" in colors)
colors.add("v")
print(colors)
colors.remove("r")
print(colors)
del colors

#Conditionals
x = 30
y = 30
# "=" Asignar * "==" Comparar
# if x < 30: 
#     print("x is less 30")
# elif x == 30:
#     print("the number is 30")
# else:
#     print("x is greater than 30")

name = "Tato"
lastname = "Coffee"

if name == "Tato":
    if lastname == "Coffee":
        print("Eres Tato")
    else:
        print("No eres Tato")
else:
    print("Tu no eres Tato Coffee")

if x > 2 and x <= 10:
    print("x >= 10")
if x > 2 or x <= 20:
    print(x <= 10)
if (not(x == y)):
    print("x==y")

# Loops
foods = ['apples', 'bread', 'cheese', 'milk']
for food in foods:
    if food == "cheese":
        print("buy for me")
        break
        continue
    print(food)

for number in range(1,9):
    print(number)

count = 4
while count <=10:
    print(count)
    count = count + 1

#Functions
def hi(name):
    print("Hi " + name)
hi("Tato")
hi("coffee")
hi("Debian")
def add(numberone, numbertwo):
    return numberone + numbertwo
print(add(10, 30))
print(add(600, 10))
print(len("hello"))
add = lambda numberOne, numberTwo: numberOne + numberTwo

print(add(10 + 30))

# Own Modules
# Thr Party Modules
# Python Modules 

from datetime import timedelta
print(timedelta(minutes=100))
# My Module
def add (n1, n2):
    print(n1 + n2)
def substrack(n1, n2):
    print(n1 - n2)

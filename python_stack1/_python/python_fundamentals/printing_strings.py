name = "Zen"
print("My Name is", name)
print("My Name is" + name)

age = 33
print("My Age is", age)
# print("My Age is" + age)

print(f"My Name is {name} and my age is {age}.")  # F string
print("My name is {} and age is {}".format(name, age)) # String.format()

x = "hello %s" % "world!"
y = "I love Python %d" % 3
print(x, y)

print(x.title())
print(y.upper())
print(y.count("o"))

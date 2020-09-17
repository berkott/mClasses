# 8.13

# Python we always technically pass by reference
# Our "primitive data" types (bool, str, int, floats) are immutable objects
# Many other objects are mutable objects, so be careful

def hot(x):
    print(joe is x)
    x[1] = "fire"
    print(joe is x)

joe = ["super hot", "barbie"]

print(f"Before function: '{joe}'")

hot(joe.copy()) # pass by value

print(f"After function: '{joe}'")

exit()

def hot(x):
    print(joe is x)
    x[1] = "fire"
    print(joe is x)

joe = ["super hot", "barbie"]

print(f"Before function: '{joe}'")

hot(joe) # pass by reference

print(f"After function: '{joe}'")

exit()

def hot(x):
    print(joe is x)
    x = x + 2
    print(joe is x)

joe = 4

print(f"Before function: '{joe}'")

hot(joe) # pass by reference

print(f"After function: '{joe}'")

exit()

# 8.12
a = ["chicken", "bob"]
b = a # assigning the same reference, aka, list object is aliased by both a and b 

print(a is b)

b[0] = "x"

print(a)

a = "chicken"
b = a

print(a is b)

b = b + "hi"

print(a)

# 8.11
a = "chicken"
b = "chicken"

print(a is b)

a = ["chicken"]
b = ["chicken"]

print(a is b)

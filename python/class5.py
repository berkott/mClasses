# 6.9 String methods
x = "happy"
print(x.upper())

# Pass by reference or pass by value

# Pass by reference: now y points to the same location in memory
# Pass by value: passes the value, not the location in memory
x = 5
y = x
x = 6
print(y) # with pass by reference y would be 6
# Lot of Python is pass by value

# === String are immutable and can't be changed ===
# Section 6.5

if "z" in "happy":
    print("happy")

if "a" > "A":
    print("a")
else:
    print("A")

string_y = "hello"
# string_y[0] = "y" # Trying to change the string, but strings are immutable

strings_y = "hello"
strings = "y" + strings_y[1:]
print(strings)

print(string_y)
print(hex(id(string_y)))

string_y = "hello2"

print(string_y)
print(hex(id(string_y)))

exit()

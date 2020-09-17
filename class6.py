# Dont forget looping through multidimensional lists
# 8.9 List and String
input_word = input()
x = input_word.split(" ")
print(x)

x_str = "chicken"

x_list = list(x_str)

print(x_list)

final_x_str = ""

print(final_x_str.join(x_list))

exit()

# 8.6 & 7 & 8
x = [3, 5, 7, 7, 10]

print(len(x))
print(max(x))
print(sum(x))

print(x.pop(1))
del x[1]
x.remove(10)
print(x)

# 8.5 List slices
x = [3, 5, 6, 6, 10]

print(x[3:])

# 8.4 List operations
x = [3, 4]
print(x + [4, 5])

# 8.3 Looping through/transversing/iterating through Lists
p_name = ["bOB", "Joe", "Michelle", "bOB", "bOB"]

i = 0

while i < len(p_name):
    print(p_name[i])
    i += 1

for name in p_name:
    print(name)

# 8.2 Mutable Lists
x = ["x", 1, 45]

x[1] = "chicken"

print(x)

# 8.1 Lists
x = ["x", 1, ["List", ["dfdf"]]]

# print(x[3])
print(x[2][1][0])
print(type(x[2][1][0]))
print(x[2][1][0].find("fdf"))

print(x)

# Chapter 8: Lists
# ===============

# 6.10
x = "happya"

print(x[x.find("x")])

x[1:4]

# 6.9 String methods
x = "happy"

# print(upper(x))
print(x.upper())
print(dir(x))

def chicken():
    return "dope"

print(chicken())

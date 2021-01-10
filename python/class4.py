# Indexing: 0 to length -1

#    0123456789
#    0       -1
x = "I like pie"

# Loop through a string with a while loop
i = 0

while i < len(x):
    print(x[i])
    i += 1

# Regular for loop can access the index values
for i in range(len(x)):
    print(i)
    print(x[i])

print("=======")

# For each loop only has the elements
for char in x:
    print(char)

print(x[2:7:2])

print(len(x[1:4]))

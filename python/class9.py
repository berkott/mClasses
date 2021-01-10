import time

ages = [10, 23, 41, 60, 36, 24, 90]
indexes_under_30_1 = []
indexes_under_30_2 = []

initial_time = time.time()
for i in range(len(ages)):
    if ages[i] < 30:
        indexes_under_30_1.append(i)
print(time.time() - initial_time)

print(indexes_under_30_1)

initial_time = time.time()
# If at end of list comprehension adds or doesnt add a value to list
indexes_under_30_2 = [i for i in range(len(ages)) if ages[i] < 30]
print(time.time() - initial_time)
print(indexes_under_30_2)

# If at beginning just changes value
print([i if ages[i] < 30 else ages[i] for i in range(len(ages))])


def mult_by_2(x):
    return x*2


print(mult_by_2(4))

# For mathematical equations, you can use lambda functions
mult = lambda x, y: x*y

print(mult(4, 5))

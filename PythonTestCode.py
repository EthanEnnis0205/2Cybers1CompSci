from functools import reduce

def f(x):
    return x**2 + 3

print(f(3))

## lambda function
y = lambda x : x**2 + 3
print(y(3))

## filter
# filter a list of numbers from 1 to 10 and only print the even numbers
print(list(filter(lambda x : x % 2 == 0, range(1, 11))))

## map
# use the map function to square every element in the list
print(list(map(lambda x : x ** 2, range(1, 11))))


## reduce
# use the reduce funtion to return the product of all the list elements
print(reduce(lambda x, y : x * y, range(1, 6)))

## sets ##
a = {1,2,3,4,5}
b = {4,5,6,7,8}

print(a | b) # print a or b
print(a & b) # print a and b
print(a - b) # print everything in a that is not in b
print(b - a) # print everything in b that is not in a

c = [2, 4, 6, 8]
d = set(c)
print(c)
print(d)

e = "CSC132"
f = set(e)
print(f)

## dictionaries ##
cars = {"Fred" : "Beetle", "Jane" : "Tesla", "Jimmy" : "Ferrari", "Bryce" : "Ford F-150"}
print(cars)

# change the value
cars["Bryce"] = "Octane"
print(cars)

# remove a key-value pair
del cars["Jane"]
print(cars)

# add a key-value
cars["Fish"] = "1997 Fish Bowl"
print(cars)

# iterate through values in the directory
for k in cars.keys():
    print(k, ":", cars[k])

for k, v in cars.items():
    print(k, ":", v)

### list comprehensions ###
squares = [x * x for x in range(1, 10) if x % 2 != 0]
print(squares)

### disctionary comprehension ###
squares_dict = {x : x for x in range(1, 10) if x % 2 != 0}
print(squares_dict)

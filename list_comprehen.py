# List comprehensions!

array = [1,2,3,4,5]

my_list = [x**2 for x in array]
print(my_list)

even = [x for x in array if x%2 == 0]
print(even)


# Set comprehension will remove duplicates!

array1 = [1,1,2,3,3,3,4]

my_set = {x for x in array1}
print(my_set)

# dictionary comprehensions! will create keys

my_dict = {x: x**2 for x in array}
print(my_dict)
#1. slice a sequence

array = [0,2,4,6,8,10,12,14,16,18,20]

print(array[5:9]) #range
print( array[5:9:2]) #using steps
print( array[:3]) # default start at 0
print( array[9:]) # default end at last item
print( array[:]) # all items

#2. reverse a sequence

my_tuple = (0,1,2,3,4,5)
print(my_tuple[::-1]) # (5,4,3,2,1,0)
print(array[::-1]) # [20,18,16,14,12,10,...]

my_string = "tasha"
print(my_string[::-1]) # ahsat

#3. reverse indexing

print(my_tuple[-1])
print(my_tuple[-1::-1])
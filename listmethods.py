dict = {1,2,3} #methods: add(), remove(), discard(), update(), 
list = [1,2,3] #methods: append(), insert(), remove(), discard()
tuple = (1,2,3)


list.append(4)
print(list)
list.insert(4,5)
print(list)
list.remove(5)
print(list)

dict.add(4)
print(dict)
dict.discard(4)
print(dict)
#dict.append(4) Python set doesn't have method append()
#print(dict)
#dict.insert(4,5) Nor insert().
#print(dict)
dict.remove(3)
print(dict)



answer = "My list turned set is: {}"
print(answer.format(list))
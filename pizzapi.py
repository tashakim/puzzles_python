from pizzapi import *

customer = Customer("T", "K", "puppy@gmail.com", "20000000") # change this
address = Address("B University", "pvd", "Rhode Island", "20906") # change this too

store = address.closet_store()

menu = store.get_menu()
menu.search(Name = "Coke")

order = Order(store, customer, address)
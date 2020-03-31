from pizzapi import *

customer = Customer("T", "K", "puppy@gmail.com", "20000000") # change this
address = Address("B University", "pvd", "Rhode Island", "20906") # change this too

store = address.closet_store()

menu = store.get_menu()
menu.search(Name = "Coke")

order = Order(store, customer, address)

#you also need to add a payment method

card = PaymentObject("10000000000", "0000", "000", "00000")
order.place(card)
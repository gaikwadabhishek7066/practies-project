menu = {
    'Pizza':100,
    'pasta':70,
    'Burgur':120,
    'Salad':50,
    'coffee':80
}
print("Welcome to PYTHON restaurant")
print("pizza:Rs100\n pasta:Rs70\n burgur:Rs120\n salad:Rs50\n coffee:Rs80")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Youritem {item_1} has been added to your order")

else:
    print(f"Orederd item {item_1} is not available yet!")

another_order = input("do you want to add another item? (yes/no) ")
if another_order == "yes":
    item_2 = input("Enter name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"item {item_2} is not available!")

third_order = input("do you want to add another item? (yes/no) ")
if third_order == "yes":
    item_3 = input("Enter name of third item = ")
    if item_3 in menu:
        order_total += menu[item_3]
        print(f"item {item_3} has been added to order")
    else:
        print(f"item {item_3} is not available!")
print(f"the total amount of items is {order_total}")
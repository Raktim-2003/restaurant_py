#define the menu of restaurant
menu  = {
    "Burger" : 100,
    "Pizza" : 200,
    "Pasta" : 300,
    "Sandwich" : 400,
    "Salad" : 500,
    "Soup" : 600,
}
# greet 
print("welcome to the R group of  restaurant")
print("Burger: Rs 100\n Pasta: Rs 300\n Pizza: Rs 200\n Sandwich: Rs 400\n Salad: 500\n Soup: Rs 600 ")

order_total=0

#500+600=1100

item_1=input("Enter the name of item what you want to order = ")

if item_1 in menu:
    order_total+=menu[item_1] # 0 + 300
    print(f"your item {item_1} has been added to your order")

else:
    print(f"ordered item {item_1} is not available yet")

another_order=input("Do you want to add another item ?(yes/no)")
if another_order=="yes":
    item_2 =input("enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item{item_2}has been added to order")
    else:
        print(f"ordered item {item_2} is not available !")
print(f"the total amount of item to pay is {order_total}")

print("your payment has been recived thank you for visiting our restaurant")

print ("visit again ! thank you")







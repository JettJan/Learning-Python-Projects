


menu = {"pizza": 3.00,
        "nachos": 2.00,
        "popcorn": 9.50,
        "fries": 1.00,
        "chips": 0.50,
        "Pretzel": 4.25,
        "soda": 2.50,
        "lemonade": 1.50}


cart = []

total = 0


print("-------MENU-------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------")


while True:
    food = input("What would you like to order? (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)


print("--------Your Order--------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total: ${total:.2f}")


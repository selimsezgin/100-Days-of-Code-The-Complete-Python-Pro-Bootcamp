print("Welcome to Python Pizza Deliveries!")
size = input("Want size pizza do you want?\n(S - M or L): ")
pepperoni = input("Do you want pepperoni on your pizza?\n(Y: Yes | N: No): ")
extraChees = input("Do you want extra cheese?\n(Y: Yes | N: No): ")

bill = 0
smallPizza = 15
mediumPizza = 20
largePizza = 25
addPepperoni_small = 2
addPepperoni_medium_large = 3
addExtraCheese = 1

if size == "s" or size == "S":
    bill += smallPizza

    if pepperoni == "y" or pepperoni == "Y":
        bill += addPepperoni_small
    elif pepperoni == "n" or pepperoni == "N":
        bill+= 0
    else:
        print("Error! Don't add!")
    
    if extraChees == "y" or extraChees == "Y":
        bill += addExtraCheese
    elif extraChees == "n" or extraChees == "N":
        bill += 0
    else:
        print("Error! Don't add!")

elif size == "m" or size == "M":
    bill += mediumPizza

    if pepperoni == "y" or pepperoni == "Y":
        bill += addPepperoni_medium_large
    elif pepperoni == "n" or pepperoni == "N":
        bill+= 0
    else:
        print("Error! Don't add!")
    
    if extraChees == "y" or extraChees == "Y":
        bill += addExtraCheese
    elif extraChees == "n" or extraChees == "N":
        bill += 0
    else:
        print("Error! Don't add!")

elif size == "l" or size == "L":
    bill += largePizza

    if pepperoni == "y" or pepperoni == "Y":
        bill += addPepperoni_medium_large
    elif pepperoni == "n" or pepperoni == "N":
        bill+= 0
    else:
        print("Error! Don't add!")
    
    if extraChees == "y" or extraChees == "Y":
        bill += addExtraCheese
    elif extraChees == "n" or extraChees == "N":
        bill += 0
    else:
        print("Error! Don't add!")

else:
    print("Error! Don't select!")


print(f"Total bill: {bill}")
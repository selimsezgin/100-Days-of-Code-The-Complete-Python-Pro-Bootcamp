print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age >= 18:
        print("Adult tickets are $12")
        bill += 12
    elif age >= 12:
        print("Youth tickets are $7")
        bill += 7
    else:
        print("Child tickets are $5")
        bill += 5

    wantPhoto = input("Do you want to have a photo take?\n(Y: Yes | N: No): ")

    if wantPhoto == "y" or wantPhoto == "Y":
        bill += 3
    elif wantPhoto == "n" or wantPhoto == "N":
        bill += 0
    else:
        print("Error: No photo will be provided!")

    print(f"Total pay: {bill}")
    
else:
    print("Sorry, you can't ride!")

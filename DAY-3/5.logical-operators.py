# Logical Operators | Mantiksal Operator
# a = 11

# print(a > 10 and a < 12)
# "and" bir logical(mantiksal) operatordur, bir kosula birden fazla sart eklenmesini saglar
# orn: "a" adlı Integer degiskenin degeri 10'dur
# a > 10 dogru, a degiskeni 10dan buyuk
#  a < 12 dogru, a degiskeni 12den kucuk
# a > 10 and a < 12 degimizde kosul olarak a 10dan buyuk ve a 12den kucuk olmalidir diye sorar
# eger cevap dogru ise if anahtarı calisir ve kosula bagli kodlar baslar
# mantiksal olarak atamda ise bool olan "True" ve "False" degerlerini cevirir

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
    elif age >= 45 and age <= 55:
    # elif 45 <= age <= 55: # 2. bir, birden fazla kosul kontrol mantigi
        bill += 0
        print("Have a free ride on us!")
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

number = int(input("What is the number you want to check: "))
moduloNumber = number % 2
# number % 2 isleminde kullanilen "%" isareti bolme islemi sirasinda, kalan sayiyi verir
# orn: 10 / 5 = 2 ve kalan kisimda herhangi bir deger olmaz, ama 7 / 3 = 2.3333... olarak devam eder
# "%" isareti burada kalan olmadigi icin 0 degerini, kalan oldugu icinde 1 degerini verir

if moduloNumber == 0:
    print("Even number")
else:
    print("Odd number")
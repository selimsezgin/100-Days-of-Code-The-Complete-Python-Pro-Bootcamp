print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? "))
person = int(input("How many people to split the bill? "))

tipPercent = tip / 100 
# tip orani yuzdelik olarak hesaplanir orn 12 girilirse 12 / 100 : 0.12 olacak

totalTipAmount = bill * tipPercent
# tutar ve tip yuzdesi carplir  orn 100 dolar tutarsa 100 * 0.12 : 12
# verilecek bahsis bulunur

totalBill = bill + totalTipAmount
# tutar ve verilecke bahsis toplanir
# orn: 100 dolar tutar, 12% ile 12 dolar bahsis ise topla 112 dolar

splitpersonPay = totalBill / person
# tutar ve bahsis sonrasi cikan topla tutar kisi sayisine bolunur
# bu bolme islemi ile kisi basi odenecek tutar hesaplanir

print(f"Each person should pay: ${splitpersonPay}")
name = input("What is your name?\nAnswer: ")
# "name" burada input() ile alinan verinin program calistigi surece tutan bir variable(degiskendir)
# name variable, input() sonrasinda herhangi farkli bir deger atanmadikca, kullanicinin girdigi veriyi tutar

print(f"Hello {name}!")
# name degiskeni burada print() kullanilarak ekrana cikti olarak verilir
# print icerisinde kullanilan f"" yapisi ise fstring'dir, fstring ile string deger ve variableler dinamik olarak kullanilabilir

nameLength = len(name)
print(f"Your name is length: {nameLength}")
# len() functionu, icerisine girilen verinin kac karakterden olustugu bilgisini vermektedir

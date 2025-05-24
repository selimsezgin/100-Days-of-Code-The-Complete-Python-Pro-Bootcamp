len("Hello")

# print(type("Hello"))
# type() functionu, icerisine eklenen degisken veya degerin data type olarak ozellgini soyler

print(type("SIUUUU"))
print(type(7))
print(type(7.0))
print(type(True))

print(int("3") + int("4"))
print(type(int("7")))
# int() functionu ile data type, Integer type donusur "4" ifadesi String bir degerdir
# int("4") olarak kullanilmasi durumunda data type String yerine Integer olur

# print(int("SIUUU"))
# ValueError: invalid literal for int() with base 10: 'SIUUU'
# eger type conversion islemini, ornegin "abc" gibi metinsel deger iceren bir String bulunuyor olabilir
# bu string ifadenin matematiksel bir karsilgi olmamasi nedeniyle int() functionu "ValueError (deger hatasi)" alacaktir

print("Number of letters in your name: " + str(len(input("Enter your name: "))))
#? print(f"Number of letters in your name: {len(input("Enter your name:"))}")
# en() function ile, input() funciton icerisine yazilan verinin karakter sayisi bulunur
# bulunan sayisi Integer bir degerdir ve String bir deger ile matematiksek bir islem yapilmaya calisilmaktadir.
# burada 3 adet cozum kullanillabilir; 1. fString kullanimi(bkz. satir 22), 2. "+" operatoru yerine "," kullanimi
# ve 3. gelen Integer degeri ValueError almamasi icin str() functionu ile String bir degere donusturmek
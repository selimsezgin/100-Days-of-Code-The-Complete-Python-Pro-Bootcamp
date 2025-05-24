# print(len("Hello"))
# len() functionu ile birlikte, icerisine eklenen String verinin kac karakterden olusdugu cikti olarak verilir

# print(len(123456))
# TypeError: object of type 'int' has no len()
# len() funcitonu yalnizca String(metinsel) ifadeleri karakter bazinda saymaktadir, sayisal verilerde kullanilamaz

#! Subscripting (Indeksleme)
# print("Hello"[0])
# String ifade sonrasinde "[1] , [2] , [0]" kullanilmasi, ilgili String ifade icerisinde o sirada bulunan karakteri getirmektedir
# Bu isleme "Subscripting" veya "Indexleme" denebilir. Indexler 0'dan baslamaktadir

# print("Hello"[len("Hello")-1])
# print("Hello"[-1])
# len() functionu ile "-1" islemi yapilmasi, mevcut uzunlugunu 1 eksiltir ve son indexin sayisine ulastirir
# bir diger yontem, eger istedigimiz index en sonuncusu ise, 0 ve ilerisi yazildigi sirada verir
# 0'dan oncesi yani negatif sayilar String ifadeyi tersen okuma mantigi ile calisir

#! String (Metinsel Deger)
print("123" + "456")
# - "" (cift tirnak) | '' (tirnak) - isaretleri arasina yazilan herhangi bir veri sayisal olarak degerlendirilmez
# cift ve tek tirnak icarisine yazilan veriler her zaman String ifade olarak degerlendirilir.

#! Integer - Int (Tam Sayi Degerleri)
print(123+456)
# eger cift ve tek tirnak icine alinmadan yazilirsa, Integer (tam sayi) deger olarak algilar
# eger matematiksel bir islem belirtilmise ilgili islemi yapar

# print(123+"456")
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# eger Integer ve String bir ifade ile matematiksel bir islem denenirse terminal "TypeError" hatasi verecektir
# Integer ve String degerler ile matematiksel islem yapilamaz

#! Large Integers (Buyuk Sayisal Deger)
print(123456789)
print(123_456_789)
# Buyuk sayisal degerlerin okunusunu prgoramcinin okumasini kolaylastirmak icin her 3 basamak arasina "_" konulabilir
# Yapilan bu islem program icerisinde herhangi bir hataya sebep olmaz

#! Floating - Float (Ondalikli Sayisal Deger)
print(3.14159)
# Float (ondalikli) degelerin data typei Int(tam sayi) degerlerden farklidir
# Ondalikli bir sayisal deger kullanilacak ise tam sayi "." ondalik kisim seklinde yazilmasi gerekir

print(3+3.15)
# Int ve Float data typeler ile matematiksel islemler saglanabilir

#! Boolean - Bool (Mantiksal Deger)
print(True)
print(False)
# Boolean yalnizca "True" ve "False" olarak 2 adet deger tutar.
# Boolean programlama icerisinde karar mekanizmasi olusturmak icin kullanilan bir mantiksal data typedir

print(3>1)
# 3>1 siralaması mantiksal olarak dogru oldugu icin, program "True" degerini donecektir

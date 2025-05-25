# if condition:
    #* do this
# else:
    #! do this

# if : kosullu islemler yapmayi saglayan bir yapidir
# if sonrasinda kontrol edilecek kosul yazilir, eger kosul saglanirsa if blogu icerisinde yer alan kod calisir
# eger if icerisinde yazan kosul saglanmaz ise, kosul saglanan kadar else blogu calisir
# else direkt olarak 

# orn: 
# i = 10 
# if i > 9: #* bu kosul basirili olarak saglanir
    # print(True) #* kosul saglandigi icin calisan kodlar
# else: #* kosul basarisiz mi kontrolu saglanır
    # print(False) #* kosul saglanmadigi icin calisan kodlar

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you can't ride!")


# if icin kullanilabilcek karsilatirma operatorlari
# ">"   |   buyuktur
# "<"   |   kucuktur
# ">="  |   buyuk veya esittir
# "<="  |   kucuk veya esittir
# "=="  |   esittir
# "!="  |   esit degildir

#! NOT: if icerisinde esittir operatoru 2 adet esittir(==) isareti ile saglanir 
#! cunku programlamada tek esittir, deger atama icin kullanilir
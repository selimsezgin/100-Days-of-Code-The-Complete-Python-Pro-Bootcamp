# print("What is your name?")
# kullanicidan girdi alabilmek icin print kullanamayiz
# bunun icin input() functionu kullanilmalidir

# input("What is your name?\nAnswer: ")
# input() functionu, print ile benzer bir yapiya sahiptir
# ancak print() functionu yalnizca ekrana cikti verebilirken
# input() functionu ayni zamanda girdi alabilmektedir
# input("A prompt for the user")


print("Hello " + input("What is your name?\nAnswer: ") + "!")
# kodlar yukaridan asagi, ve icten disa dogru calisan bir yapiya sahiptir
# bu kodda print() funcitonu icerisinde ayni zamanda bir input() functionu calistirilmaktadir
# program baslatildiginda once print() functionun icerisine, sonra input() functionun icerisine girer
# eger icinde daha fazla function yer almiyor ise, bu sefer en icten disa dogru calistirarak ilerler
# basit bir ornek ile, once merdivenden asagi iniyor ve en alt basamaktan istedigibi alip, en ust basamaga geri gidiyor


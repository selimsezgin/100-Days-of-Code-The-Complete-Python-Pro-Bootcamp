bmi = 94 / 1.75**2
print(bmi)
# vucut kitle indexi hesaplama

print(int(bmi))
# float olan degeri integera cevirme, ondaliklar gider yalnizca tam sayi

print(round(bmi))
# round() functionu, ondalikli sayiyi Integera cevirir ancak, ondalik durumuna gore bir alt veya bir ust sayiya yuvarlar

print(round(bmi, 3))
# round() functionu, icerisinde ondalikli deger ve "ndigits" adinda 2. bir deger alir
# aldigi bu 2. deger ondalikli sayiyi yuvarlamak yerine, ondalik kac basamakli olacaksa belirtilir,
# orn: round(3.14156, 2) : 3.14 olarak cikti verecektir

score = 0

score += 3
# score = score + 1 islemini score +=1 ile kisa bir sekilde yapar

score -= 1
# score = score - 1 islemi

score *= 1
# score = score * 1 islemi

score /= 1
# score = score / 1 islemi


print(f"Your score is: {score}\nYour BMI is: {round(bmi, 2)}")
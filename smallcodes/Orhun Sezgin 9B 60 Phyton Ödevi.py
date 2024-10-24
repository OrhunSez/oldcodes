print("Merhaba! Ben Boncuk. Beni Orhun Sezgin kodladı :)")
import time
time.sleep(2)

print ("Bugün seninle vücut kitle endeksini hesaplayacağız. Hadi başlayalım!")
import time
time.sleep(2)

print("Adın ne?")
ad=input()
import time
time.sleep(1)

print(("Merhaba"),(ad),("kaç yaşındasın?"))
yaş=int(input())
import time
time.sleep(1)

print(("Peki"),("bana kaç kilo olduğunu söyleyebilir misin?"))
kilo=int(input())
import time
time.sleep(1)

print(("Son olarak"),(ad),("senden boyunu santimetre cinsinden öğrenebilir miyim? (Örn: 172)"))
boy=float(input())
import time
time.sleep(2)

boyboy = boy*boy/10000
sonuc = kilo/boyboy

print ("Bana birkaç saniye ver, hesaplıyorum...")
import time
time.sleep(3)

print("İşte vücut kitle endeksi sonucun:")
import time
time.sleep(1)

print (sonuc)
import time
time.sleep (1)

if float(sonuc) <= float(18.8) :
 print("Zayıfsın")

if float(18.8) < float(sonuc) <= int(25) :
 print("Normalsin")

if int(25) < float(sonuc) <= int(30) :
 print("Biraz kilolusun")

if int(30) < float(sonuc) :
 print("Obezsin! Hiç iyi değil...")

import time
time.sleep(2)

print ("Çıkmak için herhangi bir tuş ve sonrasında 'enter' tuşuna basabilirsin :)")
input()


 

 


 



  


 


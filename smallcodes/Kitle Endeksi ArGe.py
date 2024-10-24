import time
time.sleep(1)

print("Merhaba! Ben Boncuk. Beni Orhun Sezgin kodladı :)")
time.sleep(2)

print ("Bugün seninle vücut kitle endeksini hesaplayacağız. Hadi başlayalım!")
time.sleep(2)

x = True
while x:
    print("Adın ne?")
    ad=input()
     
    time.sleep(1)

    print(("Merhaba"),(ad),("kaç yaşındasın? (Lütfen bir sayı değeri giriniz. örn:23)"))
    yas=float(input())

    if float(yas) < float(1) or float(yas) > float(95):
        print("Girdiğin yaş sistem tarafından desteklenmemektedir.")
        time.sleep(1)
        print("Program kapanıyor.")
        time.sleep(1)
        break

    time.sleep(1)

    print("Peki bana kaç kilo olduğunu söyleyebilir misin? (Örn:62)")
    kilo=float(input())

    if float(kilo) < float(10) or float(kilo) > 200:
        print("Girdiğin kilo sistem tarafından desteklenmemektedir.")
        time.sleep(1)
        print("Program kapanıyor")
        time.sleep(1) 
        break
   	
    time.sleep(1) 

    print(("Son olarak"),(ad),("senden boyunu santimetre cinsinden öğrenebilir miyim? (Örn: 172)"))
    boy=float(input())
    
    time.sleep(2)

    boyboy = boy*boy/10000
    sonuc = kilo/boyboy

    print ("Bana birkaç saniye ver, hesaplıyorum...")
    time.sleep(2)

    print("İşte vücut kitle endeksi sonucun:")
    time.sleep(1)

    print (sonuc)
    time.sleep (1)
 

    if float(sonuc) <= float(18.8) :
     print("Zayıfsın")

    elif float(18.8) < float(sonuc) <= int(25) :
     print("Normalsin")

    elif int(25) < float(sonuc) <= int(30) :
     print("Biraz kilolusun")

    else :
     print("Obezsin! Biraz daha sağlıklı beslenmeni öneririm :)")

    time.sleep(2)

    print ("Tekrar denemek için x'e, programı kapatmak için y'ye bas :).")
    a=input()
    if a == "y":
        x = False
    elif a == "x":
        x = True
    else:
        print("Lütfen x veya y tuşuna bas :)")
        b=input()
        if b == "y":
          x = False
        elif b == "x":
          x = True
        else:
          print("Aaa, yeter ama... gidiyorum ben :(")
          x = False

print("canım muzmim")
input()

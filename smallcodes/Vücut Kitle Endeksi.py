import time

print("Merhaba! Ben Boncuk. Beni Orhun Sezgin kodladı :)")
time.sleep(1)

print ("Bugün seninle vücut kitle endeksini hesaplayacağız. Hadi başlayalım!")
time.sleep(1)

x = True
while x:
    print("Adın ne?")
    ad = input()

    print(("Merhaba"),(ad),("kaç yaşındasın?"))
    yas = float(input())
    
    time.sleep(1)

    print("Peki bana kaç kilo olduğunu söyleyebilir misin?")
    kilo = int(input())

    if float(kilo) < float(10) or float(kilo) > 200:
        print('Geçersiz kilo')
        print("Program kapanıyor")
        time.sleep(1) 
        break
   	
    print(("Son olarak"),(ad),("senden boyunu santimetre cinsinden öğrenebilir miyim? (Örn: 172)"))
    boy = int(input())

    boyboy = boy*boy/10000
    sonuc = kilo/boyboy

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
     print("Obezsin! Biraz daha sağlıklı beslenmeni öneririm ")

    import time
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

            
        
 


 

 


 



  


 


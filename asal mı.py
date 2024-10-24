import keyboard
import time

print("Asal sayı denetleyicisi ve bölen ayırıcısına hoş geldiniz")


bolenler = []
x = True

while x:

    y = True

    print("Sayınızı giriniz")
    while True:
        try:
            i = int(input())
            break
        except:
            print("Lütfen bir sayı giriniz")
            continue
            
    while keyboard.is_pressed("q") == False:
        liste = list(range(1,i+1))
        #print(liste)   #burda o sayıya kadarki tüm sayılar yazılır
        for sayi in liste:
            if i%sayi == 0: #burda o listedeki tüm sayılara bölme işlemi yapılır
                #print(i)   #ve eğer bölme işlemi kalansız gerçekleşirse onun bir
                #print(sayi) #böleni kabul edilip bölenler listesine alınır
                bolenler.append(sayi)
                    
        break
    print("Bu sayının bölenleri:")
    print(bolenler)

    bolensayisi = len(bolenler)

    if bolensayisi == 2:
        print(str(i) + " asal bir sayı")

    elif bolensayisi >= 2:
        print(str(i) + " asal bir sayı değil")

    bolenler.clear()

    while y:
        print("Tekrar? (e veya h tuşlayınız)")
        cvp = input()
        if cvp in "Ee":
            break
        if cvp in "Hh":
            x = False
            y = False
        else:
            print("Lütfen e veya h tuşlayınız")
            time.sleep(0.5)
            continue

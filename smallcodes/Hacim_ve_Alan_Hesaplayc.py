from math import sqrt as kok
from math import pi as pi
import time
evet = ["e", "evet", "evt"]
hayır = ["h", "hayır", "hyr"]
sayikare = (lambda x: x**2)
dairealan = (lambda x: pi*(x**2))
uclu = (lambda x,y,z: x*y*z)
ikili = (lambda x,y: x*y) 
sayikup = (lambda x: x**3)
dairecevre = (lambda x: 2*pi*x)
hipotenus = (lambda x,y: kok((x**2)+(y**2)))
#print("İşlemleri görmek ister misiniz? (e veya h)")
#d = input()
t = True
t1 = True
t2 = True
print("Hacim ve alan hesaplayıcıya hoş geldiniz.")
while t:
    print("Hesaplamak istediğiniz türü seçin(Hacim için 1'i alan için 2'yi tuşlayın)")
    print("Çıkmak için 3'ü tuşlayınız.")
    cvp = input()
    if cvp == "1":
        print("Hesaplamak istediğiniz geometrik cismi seçiniz: \n1 - Küre \n2 - Üçgen Prizma \n3 - Dikdörtgen Prizma \n4 - Küp \n5 - Silindir \n6 - Koni \n7 - Piramit")
        b = input()
        
        while t1:
            if b == "1":
                while True:
                    try:
                        x = int(input("Kürenin yarıçapı ="))
                        break
                    except ValueError:
                        print("Lütfen bir sayı giriniz.")
                        continue
                kcvp = ((dairealan)(x))*(x*4/3)
                print("Hacim =",kcvp) 
                break

            elif b == "2":
                print("Üçgenin yükseklik uzunluğunu biliyor musunuz?")
                k = input()
                if k.lower() in evet:
                    while True:
                        try:
                            x = int(input("Üçgenin yüksekliği = "))
                            y = int(input("Üçgenin taban uzunluğu = "))
                            z = int(input("Prizmanın yüksekliği = "))
                            break
                        except ValueError:
                            print("Lütfen bir sayı giriniz.")
                            continue
                    upcvp = ((uclu)(x,y,z))/2
                    print("Hacim = ", upcvp)
                    break
                
                elif k.lower() in hayır:
                    while True:
                        try:
                            x = int(input("Üçgenin 1. kenar uzunluğu = "))
                            y = int(input("Üçgenin 2. kenar uzunluğu = "))
                            z = int(input("Üçgenin 3. kenar uzunluğu = "))
                            h = int(input("Prizmanın yüksekliği = "))
                            break
                        except ValueError:
                            print("Lütfen bir sayı giriniz.")
                            continue
                    u = (x+y+z)/2
                    upcvp = (kok((u)*(u-x)*(u-y)*(u-z)))*h
                    print("Hacim = ", upcvp)
                    break
            
            elif b == "3":
                while True:
                    try:
                        x = int(input("Prizmanın 1. kenarının uzunluğu = "))
                        y = int(input("Prizmanın 2. kenarının uzunluğu = "))
                        z = int(input("Prizmanın 3. kenarının uzunluğu = "))
                        break
                    except ValueError:
                        print("Lütfen bir sayı giriniz.")
                        continue

                dpcvp = ((uclu)(x,y,z))
                print("Hacim = ", dpcvp)
                break
            
            elif b == "4":
                while True:
                    try:
                        x = int(input("Küpün bir kenarının uzunluğu = "))
                        break
                    except ValueError:
                        print("Lütfen bir sayı giriniz.")
                        continue
                
                kcvp = x**3
                print("Hacim = ", kcvp)
                break
        
            elif b == "5":
                while True:
                    try:
                        x = int(input("Silindirin yarıçapı = "))
                        h = int(input("Silindirin yüksekliği = "))
                        break
                    except ValueError:
                        print("Lütfen bir sayı giriniz.")
                        continue
                scvp = ((dairealan)(x))*h
                print("Hacim = ", scvp)
                break   

            elif b == "6":
                while True:
                    try:
                        x = int(input("Koninin yarıçapı = "))
                        h = int(input("Koninin yüksekliği = "))
                        break
                    except ValueError:
                        print("Lütfen bir sayı giriniz.")
                        continue
                kcvp = ((dairealan)(x))*h/3
                print("Hacim = ", kcvp)
                break

            elif b == "7":
                print("Piramidin tabanı kare mi?")
                cvp = input()
                if cvp.lower() in evet:   
                    while True:
                        try:
                            x = int(input("Piramidin tabanının bir kenar uzunluğu = "))
                            h = int(input("Piramidin yüksekliği = "))
                            break
                        except ValueError:
                            print("Lütfen bir sayı giriniz.")
                            continue
                    pcvp = ((sayikare)(x))*h/3
                    print("Hacim = ", pcvp)
                    break

                elif cvp.lower() in hayır:
                    while True:
                        try:
                            x = int(input("Piramidin tabanının birinci kenar uzunluğu = "))
                            y = int(input("Piramidin tabanının ikinci kenar uzunluğu = "))
                            z = int(input("Piramidin yüksekliği = "))
                            break
                        except ValueError:
                            print("Lütfen bir sayı giriniz.")
                            continue
                    pcvp = ((uclu)(x,y,z))/3
                    print("Hacim = ", pcvp)
                    break

                else:
                    print("Lütfen evet veya hayır giriniz.")
                    continue
                    
            else:
                print("Lütfen 1 ile 7 arasında bir sayı tuşlayınız.")
                break
            
    elif cvp == "2":
        print("Hesaplamak istediğiniz geomtrik cismi seçiniz: \n1 - Daire \n2 - Üçgen \n3 - Dikdörtgen \n4 - Kare \n5 - Yamuk \n6 - Küre \n7 - Üçgen Prizma \n8 - Dikdörtgen Prizma \n9 - Kare Prizma  \n10 - Küp \n11 - Silindir \n12 - Koni \n13 - Düzgün Piramit")
        c = input()
            
        while t2:
            if c == "1":
                while True:
                    try:
                        x = int(input("Dairenin yarıçapı = "))
                        break
                    except ValueError:
                        print("Lütfen bir sayı giriniz.")
                        continue
                dcvp = ((dairealan)(x))
                print("Alan = ", dcvp)
                break   
            
            elif c == "2":
                print("Üçgenin yükseklik uzunluğunu biliyor musunuz?")
                k = input()
                if k.lower() in evet:
                    while True:
                        try:
                            x = int(input("Üçgenin yüksekliği = "))
                            y = int(input("Üçgenin taban uzunluğu = "))
                            break
                        except ValueError:
                            print("Lütfen bir sayı giriniz.")
                            continue
                    ucvp = ((ikili)(x,y))/2
                    print("Alan = ", ucvp)
                    break
                
                elif k.lower() in hayır:
                    while True:
                        try:
                            x = int(input("Üçgenin 1. kenar uzunluğu = "))
                            y = int(input("Üçgenin 2. kenar uzunluğu = "))
                            z = int(input("Üçgenin 3. kenar uzunluğu = "))
                            break
                        except ValueError:
                            print("Lütfen bir sayı giriniz.")
                            continue
                    u = (x+y+z)/2
                    ucvp = (kok((u)*(u-x)*(u-y)*(u-z)))
                    print("Alan = ", ucvp)
                    break

            elif c == "3":
                while True:
                    try:
                        x = int(input("Dikdörtgenin uzun kenarı = "))
                        y = int(input("Dikdörtgein kısa kenarı = "))
                        break
                    except ValueError:
                        print("Lütfen bir sayı giriniz.")
                        continue
                    
                
                if x > y:
                    dcvp = ((ikili)(x,y))
                    print("Alan = ", dcvp)
                    break

                elif x < y:
                    print("Uzun kenar kısa kenardan kısa olamaz.")
                    continue

                elif x == y:
                    print("Galiba kare hesaplamak istediniz. İşte sonuç = ")
                    dcvp = ((ikili)(x,y))
                    print("Alan = ", dcvp)
                    break

            elif c == "4":
                while True:
                    try:
                        x = int(input("Karenin bir kenarı = "))
                        break
                    except ValueError:
                        print("Lütfen bir sayı giriniz.")
                        continue
                    
                kacvp = ((sayikare)(x))
                print("Alan = ", kacvp)
                break
                
            elif c == "5":
                while True:
                    try:
                        x = int(input("Yamuğun alt kenarı = "))
                        y = int(input("Yamuğun üst kenarı = "))
                        h = int(input("Yüksekliği = "))
                        break
                    except ValueError:
                        print("Lütfen bir sayı giriniz.")
                        continue
                    
                ycvp = ((x+y)/2)*h
                print("Alan = ", ycvp)
                break

            elif c == "6":
                while True:
                    try:
                        x = int(input("Kürenin yarıçapı = "))
                        break
                    except ValueError:
                        print("Lütfen bir sayı giriniz.")
                        continue
                kcvp = ((dairealan)(x))*4
                print("Alan = ", kcvp)
                break

            elif c == "7":
                while True:
                    try:
                        x = int(input("Üçgenin 1. kenar uzunluğu = "))
                        y = int(input("Üçgenin 2. kenar uzunluğu = "))
                        z = int(input("Üçgenin 3. kenar uzunluğu = "))
                        h = int(input("Üçgen prizmanın yüksekliği = "))
                        break
                    except ValueError:
                        print("Lütfen bir sayı giriniz.")
                        continue
                u = (x+y+z)/2
                ucvp = 2*(kok((u)*(u-x)*(u-y)*(u-z)))
                dicvp = (x+y+z)*h
                print("Alan = ", ucvp + dicvp)
                break

            elif c == "8":
                while True:
                    try:
                        x = int(input("Dikdörtgenin uzun kenarı = "))
                        y = int(input("Diktörtgenin kısa kenarı = "))
                        h = int(input("Dikdörtgenler prizmasının yüksekliği = "))
                        break
                    except ValueError:
                        print("Lütfen bir sayı giriniz.")
                        continue
                xy = ((ikili)(x,y))*2
                xh = ((ikili)(x,h))*2
                yh = ((ikili)(y,h))*2
                if x > y:
                    print("Alan = ", xy + xh + yh)
                    break

                elif x < y:
                    print("Uzun kenar kısa kenardan kısa olamaz.")
                    continue
                
                elif y == x and h == x:
                    print("Galiba küp hesaplamak istediniz. İşte sonuç = ")
                    print("Alan = ", xy*3)
                    break

                elif x == y:
                    print("Galiba kare prizma hesaplamak istediniz. İşte sonuç = ")
                    print("Alan = ", xy + xh + yh)
                    break

            elif c == "9":
                while True:
                    try:
                        x = int(input("Karenin bir kenar uzunluğu = "))
                        h = int(input("Kare prizmanın yüksekliği = "))
                        break
                    except ValueError:
                        print("Lütfen bir sayı giriniz.")
                        continue
                xh = ((ikili)(x,h))*2
                xkare = ((sayikare)(x))*2
                
                if x != h:   
                    print("Alan = ", xh*2 + xkare)
                    break
                
                elif h == x:
                    print("Galiba küp hesaplamak istediniz. İşte sonuç = ")
                    print("Alan = ", xh*3)
                    break

            elif c == "10":
                while True:
                    try:
                        x = int(input("Küpün bir ayrıtı = "))
                        break
                    except ValueError:
                        print("Lütfen bir sayı giriniz.")
                        continue
                kcvp = ((sayikare)(x))*6
                print("Alan = ", kcvp)
                break

            elif c == "11":
                while True:
                    try:
                        x = int(input("Silindirin yarıçapı = "))
                        h = int(input("Silindirin yüksekliği = "))
                        break
                    except ValueError:
                        print("Lütfen bir sayı giriniz.")
                        continue
                dalan = ((dairealan)(x))*2
                halan = ((dairecevre)(x))*h
                print("Alan = ", dalan + halan)
                break

            elif c == "12":
                """
                while True:
                    try:
                        x = int(input("Koninin yarıçapı = "))
                        h = int(input("Koninin yüksekliği = "))
                        break
                    except ValueError:
                        print("Lütfen bir sayı giriniz.")
                        continue
                dalan = ((dairealan)(x))
                halan = ((dairecevre)(x))*h
                print("Alan = ", dalan + halan)
                break
            """
                print("Burası daha eklenmedi")
                break

            elif c == "13":
                while True:
                    try:
                        x = int(input("Karenin bir kenar uzunluğu = "))
                        h = int(input("Piramidin yüksekliği = "))
                        break
                    except ValueError:
                        print("Lütfen bir sayı giriniz.")
                        continue
                kalan = ((sayikare)(x))
                y = ((hipotenus(x/2,h)))
                yalan = ((ikili)(x,y))*2
                print("Alan = ", kalan + yalan)
                break
                
            else:
                print("Lütfen 1 ile 12 arasında bir sayı tuşlayınız.")
                continue
            
    elif cvp == "3":
        print("Program kapanıyor...")
        time.sleep(2)
        break


    else:
        print("Lütfen 1 veya 2'yi tuşlayınız.")
        continue    

import time

print("Mod hesaplayıcıya hoş geldiniz.")

def modlandınız(x, y):
    ymod = x%y
    return ymod

x = True
k = 0

while x:

    y = True

    while True:

        z = True

        try:
            print("Sayınızı giriniz")
            sayı = int(input())

            print("Sayınızın üssünü giriniz.")
            us = int(input())

            print("Modunuzu giriniz.")
            mod = int(input())
            
        except ValueError:
            print("Lütfen girdiğiniz değerlerin sayı olmasına dikkat edin.")
            time.sleep(1)
            continue
        
        if us == 1:
            cvp1 = sayı%mod
            print(str(sayı) + " = " +str(cvp1) + " (mod " + str(mod) + ")")
            break

        elif us >= 2:
            cvp1 = sayı%mod
            print(str(sayı) + " = " +str(cvp1) + " (mod " + str(mod) + ")")

            for i in range(us):
                cvp4 = cvp1**(i+1)
                if cvp4 > mod:
                    cvp4 = modlandınız(cvp4, mod)

                print(str(cvp1) + "^" + str(i+1) + " = " + str(cvp1**(i+1)) + " = " + str(cvp4) + " (mod " + str(mod) + ")")
                #print(cvp4)

                i+=1

                if i == us:
                    cvp2 = cvp1**i
                    cvp3 = cvp2%mod
                    print(str(sayı) + "^" + str(us) + " = " + str(cvp2) + " = " + str(cvp3) + " (mod " + str(mod) + ")")
                    break
                
                elif cvp4 == 1:
                    cvp5 = modlandınız(us, i)
                    print("Döngü tamamlandı.")
                    print(str(us) + " = " + str(cvp5) + " (mod " + str(i) + ")")
                    print("Seçilmesi gereken üs: " + str(cvp1) + "^" + str(cvp5))
                    #print(cvp5)
                    break
                    
                          
            break
        
        elif us == 0:
            print("Sonucunuz 1 çünkü üssünüz sıfır. 1 bütün modlarda 1'dir.")
            break

        else:
            print("Lütfen üssünüzün tamsayı olmasına dikkat ediniz.")
            continue

    while y:
        print("Bir daha denemek isterseniz 1, aksi taktirde 2 yazınız.")
        cevap = input()
        if cevap == "1":
            y = False
            x = True
        elif cevap == "2":
            print("Program kapanıyor...")
            time.sleep(1)
            y = False
            x = False
        else:
            print("Lütfen 1 veya 2 tuşlayınız.")
            time.sleep(1)
            continue

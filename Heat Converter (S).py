
import time
degerler = ["k", "c", "f", "K", "C", "F"]
evet = ["evet", "Evet", "e", "E", "yes", "y", "Y"]

while True:
    print("Girilen değer? (K,C,F)")
    a = input()
    if not a in degerler:
        print("Geçersiz değer")
        time.sleep(1)
        continue

    print("Çıkan değer? (K,C,F)")
    b = input()
    if not b in degerler:
        print("Geçersiz değer")
        time.sleep(1)
        continue

    print("Yapılan işlemi görmek ister misiniz?")
    c = input()

    print("Sıcaklık?")
    s = int(input())

    
    if a == "k":
        if b == "c":
            s1 = s-273.15
            print(s1)
            time.sleep(1)
            if c in evet:
                print(s1,"=",s,"-273.15")
                

        elif b == "f":
            s2 = (180*(s-273.15)/100)+32
            print(s2)
            time.sleep(1)
            if c in evet:
                print(s2, "=", "(180*(", s, "-273.15)/100)+32")
                

    elif a == "c":
        if b == "k":
            s3 = s+273.15
            print(s3)
            time.sleep(1)
            if c in evet:
                print(s3, "=", s,"+273.5")
                

        elif b == "f":
            s4 = (180*s/100)+32
            print(s4)
            time.sleep(1)
            if c in evet:
                print(s4, "=","(180*", s, "/100)+32")
        

    elif a == "f":
        if b == "c":
            s5 = 100*(s-32)/180
            print(s5)
            time.sleep(1)
            if c in evet:
                print(s5, "=","100*(", s, "-32)/180")
               
    

        elif b == "k":
            s6 = (100*(s-32)/180)+273.15
            print(s6)
            time.sleep(1)
            if c in evet:
                print(s6, "=","(100*(", s, "-32)/180)+273.15")
                
        
    print("Tekrar?")
    t = input()
    if t in evet:
        continue

    else:
        break

print("Program kapanıyor...")
time.sleep(1.5)




    
                    

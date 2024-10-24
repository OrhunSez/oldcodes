import time
x = True
while x:
    print("Girilen değer? (K,C,F)")
    a = input()

    print("Çıkan değer? (K,C,F)")
    b = input()

    print("Sıcaklık?")
    s = int(input())

    if a == "k" and b == "c":
        s1 = s-273.15
        print(s1)
        time.sleep(1)
        break

    elif a == "k" and b == "f":
        s2 = (180*(s-273.15)/100)+32
        print(s2)
        time.sleep(1)
        break

    elif a == "c" and b == "k":
        s3 = s+273.15
        print(s3)
        time.sleep(1)
        break

    elif a == "c" and b == "f":
        s4 = (180*s/100)+32
        print(s4)
        time.sleep(1)
        break

    elif a == "f" and b == "c":
        s5 = 100*(s-32)/180
        print(s5)
        time.sleep(1)
        break

    elif a == "f" and b == "k":
        s6 = (100*(s-32)/180)+273.15
        print(s6)
        time.sleep(1)
        break

    else:
        print("Geçersiz değer(ler)")
        time.sleep(1)
        continue
    

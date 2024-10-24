
import time

print("Tc kimlik no doğrulayıcıya hoşgeldiniz. Bu programımızda hiçbir veri veya bilgi toplanmamaktadır ")

def bibydtoplam(liste):
    b = int(liste[0])
    i = int(liste[2])
    be = int(liste[4])
    y = int(liste[6])
    d = int(liste[8])
    return b + i + be + y + d

def idastoplam(liste):
    ik = int(liste[1])
    do = int(liste[3])
    a = int(liste[5])
    s = int(liste[7])
    return ik + do + a + s

def ilkontoplam(liste):
    b = int(liste[0])
    i = int(liste[2])
    be = int(liste[4])
    y = int(liste[6])
    d = int(liste[8])
    ik = int(liste[1])
    do = int(liste[3])
    a = int(liste[5])
    s = int(liste[7])
    on = int(liste[9])
    return  b + i + be + y + d + ik + do + a + s + on

evet = ["e", "evet", "evt"]
hayır = ["h", "hayır", "hyr"]
tclist = []
i1 = []
i2 = []
i3 = []
i4 = []

x = True

while x:
    
    y = True

    print("Tc kimlik numaranızı giriniz.")
    tc = input()
    if tc.isdigit() == False:
        print("Lütfen tc kimlik numaranıza sadece sayı giriniz.")
        continue

    elif not len(tc) == 11:
        print("Tc kimlik numaranıza eksik ya da fazla sayı girdiniz.")
        continue

    tclist.extend(tc.strip())

    print("Tc kimlik numaranız:", tc)
    bibyd7 = bibydtoplam(tclist) * 7
    bibyd8 = bibydtoplam(tclist) * 8
    idas = idastoplam(tclist)
    idas9 = idastoplam(tclist) * 9
    ilkon = ilkontoplam(tclist)
    islem1 = bibyd7 + idas9
    islem2 = bibyd7 - idas

    i1.extend(str(islem1).strip())
    i2.extend(str(islem2).strip())
    i3.extend(str(ilkon).strip())
    i4.extend(str(bibyd8).strip())

    if i1[len(i1)-1] == tclist[9] and i2[len(i2)-1] == tclist[9] and i3[len(i3)-1] == tclist[10] and i4[len(i4)-1] == tclist[10]:
        print("Geçerli TC Kimlik Numarası")    
    else:
        print("Geçersiz TC Kimlik Numarası.")
        
    i1.clear()
    i2.clear()
    i3.clear()
    tclist.clear()

    while y:
        print("Bir daha sorgulamak isterseniz 'e', aksi taktirde 'h' yazınız.")
        cevap = input()
        if cevap.lower() in evet:
            y = False
            x = True
        elif cevap.lower() in hayır:
            print("Program kapanıyor...")
            time.sleep(1)
            y = False
            x = False
        else:
            print("Lütfen 'e' veya 'h' harflerine basınız.")
            time.sleep(1)
            continue

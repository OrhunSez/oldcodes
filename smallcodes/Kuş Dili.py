
import time
lia = []
sesli = ["a", "e", "ı", "i", "o", "ö", "u", "ü", "A", "E", "I", "İ" ,"O", "Ö", "U", "Ü"] 
evet = ["e", "evet", "evt"]
hayır = ["h", "hayır", "hyr"]

xacık = True # x açık

while xacık:

    yacık = True # y açık
    
    print("Kuş diline çevirmek istediğiniz metni girin.")
    a = input()

    lia.extend(a.strip())
    #print(lia)

    for harf in lia:
        if harf in sesli:
            yer = lia.index(harf)
            if harf.isupper():
                lia.pop(yer)
                lia.insert(yer , harf+"G"+harf)
            else:
                lia.pop(yer)
                lia.insert(yer, harf+"g"+harf)
                
        else:
            continue

    print("".join(lia))
    lia.clear()

    while yacık:
        print("Bir daha denemek isterseniz 'e', aksi taktirde 'h' yazınız.")
        cevap = input()
        if cevap.lower() in evet:
            yacık = False
            xacık = True
        elif cevap.lower() in hayır:
            print("Program kapanıyor...")
            time.sleep(1)
            yacık = False
            xacık = False
        else:
            print("Lütfen 'e' veya 'h' harflerine basınız.")
            time.sleep(1)
            continue

    

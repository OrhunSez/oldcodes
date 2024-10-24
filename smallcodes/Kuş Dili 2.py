
lic = []
sesli = ["a", "e", "ı", "i", "o", "ö", "u", "ü",]

print("Türkçeye çevirmek istediğiniz metni girin.")
c = input()
c1 = c.lower()

lic.extend(c1.strip())
print(lic)

for harf2 in lic:
    if harf2 in sesli:
        print(harf2)
        print(lic.index(harf2))
        # harflerin "g"li halinin silinip yerine sadece kendisinin
        #kalması sağlanmalı.

    

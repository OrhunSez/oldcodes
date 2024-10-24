def degis (y):
    x = (y*365)
    deri = int(x / 27) #kez yenilenmdi
    karaciger = int(x / 337) #kez yenilendi
    yağ = int(x / 2920) #kez yenilendi
    mide = int(x / 73) #kez yenilendi
    ter = int(x * 100)/1000 #litre ter
    gozyası = int(x * 3)/100 #litre göz yası
    kan = int(x * 22000)/1000000 #litre kan
    katıdıskı = int(x * 30)/10000 #kg
    sıvıdıskı = int(x * 200)/10000 #litre
    nefes = int(x * 10)/100 #milyon kez
    gozkırpma = int(x * 6)/1000 #milyon kez
    kalp = int((x * 37))/1000#milyon kez

    print("Şu Ana Kadar Derin {} kez yenilendi.".format(deri))
    print("Şu Ana Kadar Karaciğerin {} kez yenilendi.".format(karaciger))
    print("Şu Ana Vicudundaki Yağ {} kez yenilendi.".format(yağ))
    print("Şu Ana Kadar Miden {} kez yenilendi.".format(mide))
    print("Şu Ana Kadar {} bin litre Ter Ürettin.".format(ter))
    print("Şu Ana Kadar {} milyon litre Kan ürettin.".format(kan))
    print("Şu Ana Kadar {} litre Gözyası ürettin.".format(gozyası))
    print("Şu Ana Kadar {} bin kg Katı Dışkı ürettin.".format(katıdıskı))
    print("Şu Ana Kadar {} bin litre Sıvı Dışkı ürettin.". format(sıvıdıskı))
    print("Şu Ana Kadar {} bin kez Nefes Aldın.".format(nefes))
    print("Şu Ana Kadar {} milyon kez Göz Kırptın.".format(gozkırpma))
    print("Şu Ana Kadar {} milyon kez Kalbin Attı.".format(kalp))
    
print ("Şu Ana Kadar Vicudunda Oluşan Ortala Şeyler")

while True: 
    yas = float(input("Yaşınızı Girin:"))

    if yas <= 0:
        continue

    degis(yas)

    input()

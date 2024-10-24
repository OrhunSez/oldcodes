





giriş="""
Gizli Dosya
"""

print(giriş)

import time
time.sleep(1)

print("(TEK DENEME HAKKIN VAR!!!)İçeriği görmek için şifre giriniz :")
şifre=input()

if şifre == "lemuzmi" :
    
    t=1

    while t==1:    

        print("Hoş geldin Le Muzmi")
        import time
        time.sleep(1)
        print("Hangi içeriği istersin(Baştaki harf olarak gir.).")
        import time
        time.sleep(1)
        print("(x)Hesap makinası")
        print("(y)Boy kilo endeski")
        print("(z)Ders notu hesaplama")
        print("(Çıkmak için 0'a bas.)")
        içerik1=input()        
        if içerik1 == "x" or içerik1 == "y" or içerik1 == "z":

            if içerik1 == "x" :
                giriş = """
                (1) topla
                (2) çıkar
                (3) çarp
                (4) böl
                (5) karesini hesapla
                (6) karekök hesapla
                """

                print(giriş)

                anahtar = 1

                while anahtar == 1:
                    soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")

                    if soru == "q":
                        print("çıkılıyor...")
                        import time
                        time.sleep(1)
                        anahtar = 0

                    elif soru == "1":
                        sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
                        sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
                        print(sayı1, "+", sayı2, "=", sayı1 + sayı2)

                    elif soru == "2":
                        sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
                        sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
                        print(sayı3, "-", sayı4, "=", sayı3 - sayı4)

                    elif soru == "3":
                        sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
                        sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
                        print(sayı5, "x", sayı6, "=", sayı5 * sayı6)

                    elif soru == "4":
                        sayı7 = int(input("Bölme işlemi için ilk sayıyı girin: "))
                        sayı8 = int(input("Bölme işlemi için ikinci sayıyı girin: "))
                        print(sayı7, "/", sayı8, "=", sayı7 / sayı8)

                    elif soru == "5":
                        sayı9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
                        print(sayı9, "sayısının karesi =", sayı9 ** 2)

                    elif soru == "6":
                        sayı10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
                        print(sayı10, "sayısının karekökü = ", sayı10 ** 0.5)

                    else:
                        print("Yanlış giriş.")
                        print("Aşağıdaki seçeneklerden birini giriniz:", giriş)



            elif içerik1 == "y" :

                anahtr=1
                
                while anahtr == 1:

                    kilo=float(input("Kilon ne kadar (Kilogram (Sayı olarak) cinsinden yaz (Çıkmak için 0'a bas.))"))

                    if float(kilo) == float(0) :
                        print("Çıkılıyor...")
                        import time
                        time.sleep(1)
                        anahtr=0
                    else:
                        boy=float(input("Boyun ne kadar (Metre (Sayı olarak) cinsinden yaz (Çıkmak için 0'a bas.))"))

                        if float(kilo) == float(0) :
                            print("Çıkılıyor...")
                            import time
                            time.sleep(1)
                            anahtr=0
                        else:                           
                            if float(kilo/boy**2)  <= float(18.8) :
                                print("Zayıfsınız.")
                                import time
                                time.sleep(1)

                            elif float(18.8) < float(kilo/boy**2) <= float(25) :
                                print("Normalsiniz.")
                                import time
                                time.sleep(1)

                            elif float(25) < float(kilo/boy**2) <= float(30) :
                                print("Hafif kilolusunuz.")
                                import time
                                time.sleep(1)

                            elif float(30) < float(kilo/boy**2) :
                                print("Obezsiniz.")
                                import time
                                time.sleep(1)

                            else:
                                print("Baştan deneyin.")
                                import time
                                time.sleep(1)
                                anahtr=1
                    
                            
                                  
                                  

                        
            elif içerik1 == "z" :

                anhtar=1

                while anhtar ==1 :
                    karne=float(input("Notun kaç?(Çıkmak için 0'a bas.)"))
                    if karne == float(0) :
                        print("Çıkılıyor...")
                        import time
                        time.sleep
                        anhtar=0


                    elif karne<float(0) or karne>float(100) :
                        print("0'dan küçük , 100'den büyük olmasın.")
                        import time
                        time.sleep(1)
                        anhtar=1



                    elif karne != float() :
                        print("Sayı olarak gir.")
                        import time
                        time.sleep(1)
                        anhtar=1

                        
                    else:
                        if karne<45 :
                            print("1")
                            import time
                            time.sleep(1)
                            print("Çok çalışmalısın.")
                            import time
                            time.sleep(1)
                            anhtar=1
                        elif karne<55 :
                            print("2")
                            import time
                            time.sleep(1)
                            print("Çalışmalısın.")
                            import time
                            time.sleep(1)
                            anhtar=1
                        elif karne<70 :
                            print("3")
                            import time
                            time.sleep(1)
                            print("Az daha çalışmalısın.")
                            import time
                            time.sleep(1)
                            anhtar=1
                        elif karne<85 :
                            print("4")
                            import time
                            time.sleep(1)
                            print("Çok güzel.")
                            import time
                            time.sleep(1)
                            anhtar=1
                        else:
                            print("5")
                            import time
                            time.sleep(1)
                            print("Harikasın.")
                            import time
                            time.sleep(1)
                            anahtar=1

                                        
        

        elif içerik1 == "0":
            print("Görüşürüz...")
            import time
            time.sleep(1)
            t=0
            




        else:
            print("Baştakileri dene lütfen Le Muzmi.")
            import time
            time.sleep(1)
            t=0




else:
    print("Yanlış şifre...")
    import time
    time.sleep(1)
    




            

            
        

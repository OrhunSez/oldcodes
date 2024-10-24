'''
print("Kaçtan başlasın")
a = int(input())


for cevp in range(3):
    print(a + 1)
    cevp+=1

#burdaki kodda kaçtan başlasın değil, girilen a değerinin bir fazlasının kaç defa yazılacağı veriliyor
'''

'''
print("Kaçtan başlasın?")
b = int(input())


while True:
    print(b+1)
    b+=1
    if b == 15:
        break

#işte şimdi oldu. burda girilen b sayısından başlayıp 21. satırda verilen sayıya gelene kadar döngü devam edicek 
#ve sonrasında duracak
'''

print("Modunuzu giriniz.")
mod = int(input())

print("Sayınızı giriniz")
sayı = int(input())

cvp = sayı%mod
print(str(sayı) + " = " +str(cvp) + " (mod " + str(mod) + ")")



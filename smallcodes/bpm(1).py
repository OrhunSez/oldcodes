import time
import os 
def clear(): os.system('clr') #online text editörde clean yapmak için 'clr' değil 'clear' kullanılıyor
bpm = int(input("bpm? : "))
delay = 60/bpm
i = 0
tur = 1
while True:
    clear()
    print(f"bpm = {bpm}, Tur = {tur}")
    while True:
        i += 1
        #print("\a")
        #normalde print("\a") komutu göktuğnun sitesinde çalışıyor ama burda sistem sesi veriyor
        print(i)
        time.sleep(delay)
        if i == 4:
            i = 0 
            break
    tur += 1 

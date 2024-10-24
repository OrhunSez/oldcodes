
from math import sqrt
import time

def ortalama(gelen_sayilar):
    miktar = len(gelen_sayilar)
    toplam = sum(gelen_sayilar)
    return toplam/miktar

yes = ["yes", "y"]
no = ["no", "n"]

list1 = []
cikartkare = []


while True:
    while True:
        print("Would you like to add a number?")
        a = input()
        if a.lower() in yes:
            print("What is your number?")
            try:
                b = int(input())
            except ValueError:
                print("Please add a valid number.")
                time.sleep(1)
                continue
            list1.append(b)
            print("Your number has been added to the list.") 
            time.sleep(1)


        elif a.lower() in no:
            print("List is completed.")
            time.sleep(2)
            break

        else:
            print("Please answer like y(yes) or n(no).")
            time.sleep(1)
            continue

    if len(list1) == 0:
        print("Please add a number to the list.")
        time.sleep(1)
        continue

    elif len(list1) - 1 == 0:
        print("Please add more than one number.")
        time.sleep(1)
        continue
    
    print("Here is your list")
    time.sleep(1)
    print(list1)
    
    print("Here is your average")
    time.sleep(1)
    ort = ortalama(list1)
    print(ort)

    for i in range(0, len(list1)):
        deger = ort - list1[i]
        deger = deger*deger
        cikartkare.append(deger)
    
    print("Here is your list of substracted and squared numbers.")
    time.sleep(1)
    print(cikartkare) #burda çıkartmaları yapılmış ve kareleri alınmış sayılar var

    toplam = sum(cikartkare)
    sonuc = sqrt(toplam/(len(list1)-1))
    
    print("Here is your result")
    time.sleep(1)
    print(sonuc)

    print("Again?")
    c = input()
    if c.lower() in yes:
        continue
    else:
        break

input()



    

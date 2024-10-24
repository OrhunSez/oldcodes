import keyboard
import time

print("Welcome to prime number detector and divisors finder")

x = 0
divisors = []
x = True

while x:

    y = True

    print("Please enter the number that you want to test")
    while True:
        try:
            i = int(input())
            break
        except:
            print("Your input is not a valid number. Try again")
            continue

    if i == 0:
        print("""0 or smaller numbers are not positive numbers, so they can't be prime.
Please try another number""")
        continue
    
    elif i <= 0:
        print("0 or smaller numbers are not positive numbers, so they can't be prime.")
        print("""This program is not able to calculate the divisors of negative numbers.
Please try another number.""")
        continue
            
    while keyboard.is_pressed("q") == False:
        lista = list(range(1,i+1))
        #print(lista)   #if you do this it will print all the numbers until the given number is printed
        for num in lista:
            if i%num == 0: #this tries to divide our number by all the numbers smaller than it
                #print(i)
                #print(sayi)
                #and if the remainder is 0 it is considered as a divider
                #and if it is a divider it is added to the dividers list
                divisors.append(num)
                    
        break
    print("The divisors of this number are:")
    print(divisors)

    num_of_divisors = len(divisors)

    if num_of_divisors == 2:
        print(f"{i} is a prime number")

    elif num_of_divisors >= 2:
        print(f"{i} is not a prime number")

    elif num_of_divisors == 1:
        print(f"{i} is not a prime number")

    divisors.clear()

    while y:
        print("Again? [enter 'y'(yes) or 'n'(no)]")
        ans = input()
        if ans in "Yy":
            break
        if ans in "Nn":
            x = False
            y = False
        else:
            print("Please enter 'y' or 'n'")
            time.sleep(0.5)
            continue

print("Program is closing...")
time.sleep(2)


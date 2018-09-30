import random
sayi=random.randint(1,100)
while True:
    sayi1 = int(input("Lütfen bir sayi giriniz :"))
    if sayi < sayi1:
        print ("büyük!!")
    elif sayi > sayi1:
        print ("küçük!!")
    elif sayi == sayi1:
        print ("Buldun!!!")
        break

from random import choice
karakterler = ["a","b","c",1,4,8]
print("Parolanizin uzunlugu kac karakter olsun?")
parolaUzunluk=int(input())
parola=""
for i in range(parolaUzunluk):
    parola+=str(choice(karakterler))
print (parola)

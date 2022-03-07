# Zadatak1
poruka = input("Unesite poruku: ")
# TODO: Zadatak ne radi za poruku koja ima izmedu 20 i 40 znakova
if poruka <= "joj":
    print("laze")
elif poruka <= "hm":
    print("laze")
elif len(poruka) <= 20:
    print("laze")
elif len(poruka) >= 40:
    print("laze")
else:
    print("ne laze")

# Zadatak2
numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
print(sum([i
           for i in numbers
           if i % 2 != 0
           ]))

# Zadatak3
jobs = ["The tester", "The cajka", "The fireman", "The surgeon", "The programmer"]
adverbs = ["somewhat", "slightly", "extremely"]
adjectives = ["happy", "crazy", "anxious", "insane", "sexy"]
hairColors = ["blond", "purple", "pink", "red"]
import random

random.shuffle(jobs)
random.shuffle(adverbs)
random.shuffle(adjectives)
random.shuffle(hairColors)
print(random.choice(jobs) + " is " + random.choice(adverbs) + " " +
      random.choice(adjectives) + " and has " + random.choice(hairColors) + " hair")

# Zadatak4

# TODO: Komentirani kod je uvijek dobro maknuti. Naravno, ne i komentare opcenito :)
# TODO: String "ino" se u rjesenju pojavljuje 2 puta, sto ne bi trebao biti slucaj

#pozvani = ["Otto", "Otto", "Neven", "Mario", "Lana", "Ana", "Tihana", "Ino", "Nikolina"]
#pozvani.sort()

pozvani = sorted([x.lower() for x in ["Ini", "Otto", "Neven", "Mario", "Lana", "Ana",
                                      "ino", "Tihana", "Ino", "Nikolina", "Ana"]])

# palindromi = list(filter(lambda x: (x.lower() == "".join(reversed(x.lower()))), pozvani))
# print("Palindromi = ", palindromi)
i = 0
while i < len(pozvani):
   #if i == i[::-1]:
    if pozvani[i] == "".join(reversed(pozvani[i])):
        #print("Jejejejejej")
        del pozvani[i]
        i = i-1
    i=i+1

print(pozvani)




# Zadatak5

# TODO: Postoji nekoliko slucajeva koji nisu pokriveni, npr. ista cijena za svakog mehanicara, negativni brojevi,
#  popust veci od 100% itd.

remen_renato = float(input("Cijena popravka remena je: "))
branik_renato = float(input("Cijena popravka branika je: "))
popust_renato = float(input("Popust iznosi (%): "))
ukupna_cijena_renato= remen_renato + branik_renato
cijena_s_popustom_renato = ukupna_cijena_renato - ukupna_cijena_renato * popust_renato / 100
print("Renato:", cijena_s_popustom_renato)

remen_marina = float(input("Cijena popravka remena je: "))
branik_marina = float(input("Cijena popravka branika je: "))
popust_marina = float(input("Popust iznosi (%): "))
ukupna_cijena_marina= remen_marina + branik_marina
cijena_s_popustom_marina = ukupna_cijena_marina - ukupna_cijena_marina * popust_marina / 100
print("Marina:", cijena_s_popustom_marina)

remen_luka = float(input("Cijena popravka remena je: "))
branik_luka = float(input("Cijena popravka branika je: "))
popust_luka = float(input("Popust iznosi (%): "))
ukupna_cijena_luka= remen_luka + branik_luka
cijena_s_popustom_luka = ukupna_cijena_luka - ukupna_cijena_luka * popust_luka / 100
print("Luka:", cijena_s_popustom_luka)

ponude_mehanicara = [cijena_s_popustom_renato, cijena_s_popustom_marina, cijena_s_popustom_luka]
min_vrijednost = min(ponude_mehanicara)

if min_vrijednost == cijena_s_popustom_luka:
    print("Najpovoljnija ponuda je kod Lukice: ", min(ponude_mehanicara), "kn")
elif min_vrijednost == cijena_s_popustom_marina:
    print("Najpovoljnija ponuda je kod Marine: ", min(ponude_mehanicara), "kn")
else:
    print("Najpovoljnija ponuda je kod Renata: ", min(ponude_mehanicara), "kn")
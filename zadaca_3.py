# Zadatak1
poruka = input("Unesite poruku: ")
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

remen_renato = float(input("Cijena popravka remena je: "))
branik_renato = float(input("Cijena popravka branika je: "))
popust_renato = float(input("Popust iznosi (%): "))
ukupna_cijena_renato= remen_renato + branik_renato
cijena_s_popustom_renato = ukupna_cijena_renato - ukupna_cijena_renato * popust_renato / 100
#mehanicar_renato = (str("Renato") + cijena_s_popustom_renato)
#print(mehanicar_renato)
print(cijena_s_popustom_renato)

remen_marin = float(input("Cijena popravka remena je: "))
branik_marin = float(input("Cijena popravka branika je: "))
popust_marin = float(input("Popust iznosi (%): "))
ukupna_cijena_marin= remen_marin + branik_marin
cijena_s_popustom_marin = ukupna_cijena_marin - ukupna_cijena_marin * popust_marin / 100
#mehanicar_marin = (str("Marin") + cijena_s_popustom_marin)
#print(mehanicar_marin)
print(cijena_s_popustom_marin)

remen_luka = float(input("Cijena popravka remena je: "))
branik_luka = float(input("Cijena popravka branika je: "))
popust_luka = float(input("Popust iznosi (%): "))
ukupna_cijena_luka= remen_luka + branik_luka
cijena_s_popustom_luka = ukupna_cijena_luka - ukupna_cijena_luka * popust_luka / 100
#mehanicar_luka = (str("Luka") + cijena_s_popustom_luka)
#print(mehanicar_luka)
print(cijena_s_popustom_luka)

#ponude = [mehanicar_renato, mehanicar_marin, mehanicar_luka]
#print("Najpovoljnija ponuda je  : ", min(ponude))

ponude_mehanicara = [cijena_s_popustom_renato, cijena_s_popustom_marin, cijena_s_popustom_luka]
print("Najpovoljnija ponuda je  : ", min(ponude_mehanicara))

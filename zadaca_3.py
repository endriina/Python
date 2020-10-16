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


pozvani = ["Otto", "Neven", "Mario", "Lana", "Ana", "Tihana", "Ino", "Nikolina"]
pozvani.sort()

palindromi = list(filter(lambda x: (x.lower() == "".join(reversed(x.lower()))), pozvani))
print("Palindromi = ", palindromi)









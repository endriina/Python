import random


name = input("Kako se zoves? ")

print("Sretno ", name)

rijeci = ['monitor', 'racunalo', 'tipkovnica', 'cesta',
         'programiranje', 'frizider', 'kuhinja', 'vrata',
         'kuhar', 'mlijeko', 'macka', 'edgar']

# Funkcija koja odabire random rijec iz liste

rijec = random.choice(rijeci)

print("Pogodi slovo")

guesses = ''

# koji je broj pokusaja
pokusaji = 10

while pokusaji > 0:

    # koliko puta igrac nije pogodio
    failed = 0

    # sva slova iz inputa igraca
    # jedno po jedno slovo
    for char in rijec:

        # usporedi to slovo sa slovom u guesses

        if char in guesses:
            print(char)

        else:
            print("_")

            # za svaku gresku increment u failure

            failed += 1

    if failed == 0:
        # ako je broj gresaka 0 user pobjeduje
        # Igra ispisuje bravo
        print("Bravo!")

        # igra ispisuje rijec koju je igrac pogadao
        print("Rijec je: ", rijec)
        break

    # ako je igrac unio krivo slovo trazi ga ga unese novo

    guess = input("pogodi slovo:")

    # svaki unos igraca sacuvaj u guesses
    guesses += guess

    # provjeri input sa slovom u rijeci
    if guess not in rijec:

        pokusaji -= 1

        # ako nema tog slova u rijeci igra ispisuje Krivo slovo
        print("Krivo slovo!")

        # ispisujemo igracu koliko pokusaja jos ima

        print("Imas jos", + pokusaji, 'pokusaja.')

        if pokusaji == 0:
            print("Zao mi je, izgubio si!")
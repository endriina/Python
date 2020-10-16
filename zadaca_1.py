#Zadatak1 - Kreiraj projekt i file
#Zadatak2
ime = "Endrina"
prezime = "Eskic"
team = ime.upper() + " " + prezime.upper()
print(team)

#Zadatak3
dan="20"
mjesec="12"
godina="1994."
datum= dan + ". " + mjesec + ". " + godina
print(datum)

#Zadatak4
import datetime
now = datetime.datetime.now()
godinaRodenja = int(input("Unesi godinu rodenja: "))
trenutnaGodina = now.year
sum = trenutnaGodina - godinaRodenja
print("Endrina Eskic ima" , sum , "godina.")
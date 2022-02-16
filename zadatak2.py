#ZADATAK 3: HEMINGWAY

autor = input("Unesite autora: ")
ime_knjige = input("Unesite ime knjige: ")
if autor <= "Hemingway" and len(ime_knjige) >= 30:
    print("Ok, tako već može")
elif autor == "Hemingway" and len(ime_knjige) >= 30:
    print("Ma jel' moguće?")
elif autor <= "" and len(ime_knjige) <= 25:
   print("Šta, nismo bili u školi?")
#elif len(poruka) >= 40:
 #   print("laze")
#else:
 #   print("ne laze")


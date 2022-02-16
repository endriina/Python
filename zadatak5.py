#ZADATAK 1: PIJANI PERO

novcanik = "540 hrk"
#print(novcanik[0:3])
peroIma = novcanik[0:3]
print(peroIma)
zenin_novcanik = "1000 hrk"
peroNema = zenin_novcanik[0:4]
#print(peroNema)

print('Unesi iznos kazne:')
x = input()

if x < peroIma:
    print("Ajme, mogao sam popiti još jedan gemišt.")
elif x >= peroIma:
    print("Nije tak ni strašno.")
elif x <= peroNema:
    print("Nije tak ni strašno.")
elif x > peroNema:
    print("Hoćeš ti reći mojoj zeni?")
else:
    print("OK")
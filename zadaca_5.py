class Tester:
    def __init__(self, ime, prezime):

        self.ime = ime
        self.prezime = prezime


class Projekt:
    def __init__(self, ime_projekta, main_Tester):

        self.ime_projekta = ime_projekta
        self.tester = main_Tester


prvi_tester = Tester(input("Unesi ime: "), input("Unesi prezime: "))
drugi_tester = Tester(input("Unesi ime: "), input("Unesi prezime: "))
print(prvi_tester.ime, prvi_tester.prezime)

prvi_projekt = Projekt(input("Unesi ime projekta: "), input("Unesi ime testera: "))
print("Project name:" + prvi_projekt.ime_projekta, "Main tester: " + prvi_projekt.tester)

f= open("projekti.txt","w+")


    #preskoci liste zasad
    # #lista = []
    #
    # #n = 2
    #
    # #for i in range(0, n):
    #
    #     projekt_naziv = Projekt.ime_projekta
    #     tester_osoba = Tester.ime, Tester.prezime
    #
    #
    # for key, value in lista.items():
    #     print(key)






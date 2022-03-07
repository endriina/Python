#ZADATAK 2: POKEDEX

# TODO: Rjesenje nije tocno, trebalo bi biti kako je napisano u zadatku,
#  tj. lista od 4 elementa poredana na isti nacin -
#  ['Bulbasaur 10', 'Charmander 10', 'Bulbasaur 100', 'Charmander 100']

Pokemon = ["Bulbasaur", "Charmander"]
Category = [10, 100]

for x in Pokemon:
    for y in Category:
        print(x, y)
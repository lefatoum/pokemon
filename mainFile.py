import pandas as pnd
import numpy as nmp
import os

pnd.set_option('display.max_columns', None)
listerDeFichiers = os.listdir("datas")
for fichier in listerDeFichiers:
    print(fichier)

nosPokemons = pnd.read_csv("datas/pokedex.csv", encoding='latin-1')
print(nosPokemons.columns.values)


print(nosPokemons.head(20))


nosPokemons['LEGENDAIRE'] = (nosPokemons['LEGENDAIRE'] == 'VRAI').astype(int)

print(nosPokemons['LEGENDAIRE'].head(800))

print(nosPokemons.shape)

print(nosPokemons.info())

print(nosPokemons[nosPokemons['NOM'].isnull()])

print(nosPokemons['NOM'][61])
print(nosPokemons['NOM'][63])